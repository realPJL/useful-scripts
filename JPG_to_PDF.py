import img2pdf

def jpg_to_pdf(jpg_path, pdf_path):
    # Convert JPG file to a PDF file
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(jpg_path))

# Example usage:
jpg_file = "example.jpg"  # Specify the path to your JPG file
pdf_file = "output.pdf"  # Specify the path to the output PDF file

jpg_to_pdf(jpg_file, pdf_file)
