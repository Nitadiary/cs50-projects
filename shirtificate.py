from fpdf import FPDF

def main():
    name = input("write your name: ")
    c_shirtificate(name)

def c_shirtificate(name):
    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()

    pdf.set_font(family="Helvetica", style="B", size=16)
    pdf.cell(0, 20, "CS50 Shirtificate", ln= True, align="C")
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    pdf.set_font(family="Helvetica", style="B", size=32)
    pdf.set_text_color(255,255,255)
    pdf.set_xy(0,120)
    pdf.cell(210, 20, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
