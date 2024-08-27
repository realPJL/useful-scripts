import PyPDF2

def merge_pdfs(pdf_list, output):
    # Create PDF Writer
    pdf_writer = PyPDF2.PdfWriter()

    # Open every PDF in list and add to writer
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    # Write all PDFs into one
    with open(output, 'wb') as out:
        pdf_writer.write(out)

# Example usage
pdfs = ['first_file.pdf', 'second_file.pdf']
output_pdf = 'output_file.pdf'
merge_pdfs(pdfs, output_pdf)
