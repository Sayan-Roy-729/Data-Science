"""
Create a PDF using fpdf. ALso add a page and add cell/text to the page.
"""

from fpdf import FPDF, XPos, YPos

# create FPDF object
# Layout ('P', 'L)
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100, 150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
# font size
pdf.set_font("helvetica", "", 16)

# add text
# w = width, if 0 then it will be entire width of the page
# h = height
# new_x & new_y helps to add next texts to the next line, not to the same line
# draw a border around the cell
pdf.cell(120, 100, "Hello World!", new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=True)

pdf.cell(80, 10, "Good Bye World!")

pdf.output("pdf_1.pdf")
