from PIL import Image
import os

def convert_webp_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, 'PNG')

def batch_convert_webp_to_png(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.webp'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f'{os.path.splitext(filename)[0]}.png')
            convert_webp_to_png(input_path, output_path)
            print(f'Converted {input_path} to {output_path}')

input_directory = 'path/to/webp/files'
output_directory = 'path/to/png/output'

batch_convert_webp_to_png(input_directory, output_directory)