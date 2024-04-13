from PIL import Image

def convert_png_to_jpeg(png_path, jpeg_path):
    try:
        # Open PNG image
        png_image = Image.open(png_path)
        
        # Convert PNG to JPEG
        rgb_image = png_image.convert('RGB')
        
        # Save as JPEG
        rgb_image.save(jpeg_path)
        
        print(f"Conversion successful. JPEG image saved at {jpeg_path}")

    except Exception as e:
        print(f"Error converting image: {e}")


def main():
    # Copy path of PNG file into quotation marks
    png_file = "input_image.png"
    
    # Copy path of JPEG file into quotation marks
    jpeg_file = "output_image.png"
    
    # Use function to convert image
    convert_png_to_jpeg(png_file, jpeg_file)

if __name__ == "__main__":
    main()
