"""
Add header to a page like Title. Add logo/images, footer
as page number and add auto page breaks once the text reaches
the end of the page.
"""
from fpdf import FPDF, XPos, YPos


class PDF(FPDF):
    # page header
    def header(self):
        # logo
        self.image("logo.png", x=10, y=8, w=25)
        # font
        self.set_font("helvetica", "B", 20)
        # padding
        self.cell(80)
        # title
        self.cell(30, 10, "Title", border=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        # line break
        self.ln(20)

    # page footer
    def footer(self):
        # set the position of the footer
        self.set_y(-15)  # negative means from the bottom
        # set font
        self.set_font("helvetica", "I", 10)
        # Page number
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Create a PDF object
pdf = PDF("P", "mm", "Letter")

# get total page numbers
pdf.alias_nb_pages()

# set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# specify font
pdf.set_font("helvetica", "BIU", 16)

pdf.set_font("times", "", 12)

for i in range(1, 41):
    pdf.cell(0, 10, f"This is line {i} :D", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("pdf_2.pdf")

