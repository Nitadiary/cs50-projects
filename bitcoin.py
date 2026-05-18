import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    url = "https://api.coincap.io/v3/assets/bitcoin"

    headers = {"Authorization" : "Bearer f94ed7767288c743a74020ed209c1ec8448f4a76c22ce671291557c9a3ae0405" }

    try:
        response = requests.get(url, headers= headers)
        response.raise_for_status()
        data = response.json()

        price = float(data["data"]["priceUsd"])
        amount = price * number
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("API connection lost")
if __name__ == "__main__":
    main()
