from PIL import Image
import os

# NOTICE: this scripts processes ALL images in the input folder
input_folder = "/path/to/images"
output_folder = "/path/to/output"

desired_size = (500, 500)

for filename in os.listdir(input_folder):
    with Image.open(os.path.join(input_folder, filename)) as img:
        img.thumbnail(desired_size)
        img.save(os.path.join(output_folder, filename))