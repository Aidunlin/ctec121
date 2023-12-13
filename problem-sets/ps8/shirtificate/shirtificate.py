import fpdf

name = input("Name: ")
pdf = fpdf.FPDF(orientation="P", format="a4")
pdf.add_page()
pdf.image("shirtificate.png", x=fpdf.Align.C)
pdf.set_text_color(255)
pdf.set_font(family="Helvetica", size=12)
pdf.cell(txt=name, align=fpdf.Align.C)
pdf.output("shirtificate.pdf")
