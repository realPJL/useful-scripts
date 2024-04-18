# pip install pdf2image
from pdf2image import convert_from_path
import os

def pdf_to_jpg(pdf_path, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Save each page as a JPG file
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"{os.path.basename(pdf_path)[:-4]}_page_{i+1}.jpg"), "JPEG")

# Example usage:
pdf_file = "example.pdf"  # Specify the path to your PDF file
output_folder = "output_images"  # Specify the folder where the JPG images will be saved

pdf_to_jpg(pdf_file, output_folder)
