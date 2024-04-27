from PIL import Image

def remove_background(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGBA (if not already in that mode)
    img = img.convert("RGBA")

    # Get the alpha channel
    datas = img.getdata()

    # Define a threshold
    threshold = 200

    # Create a new transparent image
    new_data = []
    for item in datas:
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0))  # Set pixel to transparent
        else:
            new_data.append(item)

    # Update the image with the new data
    img.putdata(new_data)

    # Save the image
    img.save(output_path, 'PNG')

if __name__ == "__main__":
    input_image_path = 'RemoveBackground.png'
    output_image_path = 'background_removed.png'
    remove_background(input_image_path, output_image_path)
