"""
Add underline of particular word(s) with in a text
"""

from PIL import ImageFont
from fpdf import FPDF


def get_text_width(text_string, font: ImageFont.truetype):
    # the 2.6 works with times
    # 3 works pretty well with arial
    # why these numbers work... I don't know
    return font.getmask(text_string).getbbox()[2] / 2.6


# create pdf object
pdf = FPDF("P", "mm", "Letter")

# add a page
pdf.add_page()

# set image font
font = ImageFont.truetype("times.ttf", 12)

# set font
pdf.set_font("times", "", 12)
text_string_1 = "Hello"
# get width of font and add it as width of cell
pdf.cell(get_text_width(text_string_1, font), 10, text_string_1)

pdf.set_font("times", "u", 12)
text_string_2 = "world"
pdf.cell(get_text_width(text_string_2, font), 10, text_string_2)

pdf.set_font("times", "", 12)
text_string_3 = "this is me"
pdf.cell(10, 10, text_string_3)

pdf.output("pdf_4.pdf")
