import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    probabilities = {p: 0.0 for p in corpus}
    num_pages = len(corpus)

    teleport_prob = (1 - damping_factor) / num_pages
    for p in probabilities:
        probabilities[p] += teleport_prob

    links = corpus[page]
    if links:
        link_prob = damping_factor / len(links)
        for link in links:
            probabilities[link] += link_prob

    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ranks = {page: 0 for page in corpus}

    current = random.choice(list(corpus.keys()))
    ranks[current] += 1

    for _ in range(1, n):
        trans_probs = transition_model(corpus, current, damping_factor)
        pages = list(trans_probs.keys())
        probs = list(trans_probs.values())
        current = random.choices(pages, weights=probs, k=1)[0]
        ranks[current] += 1

    total = sum(ranks.values())
    for page in ranks:
        ranks[page] = ranks[page] / total

    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    ranks = {page: 1.0 / num_pages for page in corpus}
    threshold = 0.001

    while True:
        new_ranks = {page: (1 - damping_factor) / num_pages for page in corpus}

        for page in corpus:
            for linking_page in corpus:
                links = corpus[linking_page]

                if len(links) == 0:
                    new_ranks[page] += damping_factor * ranks[linking_page] / num_pages

                elif page in links:
                    new_ranks[page] += damping_factor * ranks[linking_page] / len(links)

        max_diff = max(abs(new_ranks[p] - ranks[p]) for p in corpus)
        ranks = new_ranks

        if max_diff < threshold:
            break

    return ranks


if __name__ == "__main__":
    main()
