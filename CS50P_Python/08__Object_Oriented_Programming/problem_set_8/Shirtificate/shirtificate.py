# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
# https://py-pdf.github.io/fpdf2/Tutorial.html#tutorial
# https://py-pdf.github.io/fpdf2/fpdf/
# pip install fpdf2
# Ask user for name and output PDF file with shirt and his name


from fpdf import FPDF

PATH = "CS50P_Python/08__Object_Oriented_Programming/problem_set_8/Shirtificate"

# claim = input("\nName: ") + " took CS50"
claim = "Marek took CS50"

# creating PDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()


# adding shirt image
pdf.set_y(60)  # moving cursor a bit lower
# width = page width
pdf.image(f"{PATH}/shirtificate.png", w=pdf.epw)


# adding page title
pdf.set_y(10)  # move cursor back to the top
pdf.set_font("helvetica", "B", 20)
pdf.cell(0, 10, "CS50 Shirtificate", center=True, align="C", border=0)


# adding claim on the shirt
pdf.set_y(100)  # move cursor down to the middle
pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica", "B", 40)
pdf.cell(0, 100, claim, center=True, align="C", border=0)


# generating PDF
pdf.output(f"{PATH}/shirtificate.pdf")
