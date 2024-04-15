import reportlab
from reportlab.pdfgen import canvas


def create_pdf(path: str, image_path: str = "images\\image_1712160105.png"):
    new_pdf = canvas.Canvas("text.pdf")

    new_pdf.drawString(250, 500, "Imagine aici")
    new_pdf.drawImage(image_path, 200, 500)
    new_pdf.save()
