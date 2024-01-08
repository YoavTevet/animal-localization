# This is the program I used to normalize all pictures and turn them to 100 by 100.
# it reduced my database from about 600 MB to about 80 MB.

from PIL import Image
import os

def resize_images(input_folder, output_folder, new_size=(100, 100)):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each file in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        
        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # Open the image
                with Image.open(input_path) as img:
                    # Resize the image
                    resized_img = img.resize(new_size)
                    
                    # Save the resized image to the output folder
                    output_path = os.path.join(output_folder, filename)
                    resized_img.save(output_path)
                    
                    print(f"Resized {filename} successfully.")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Replace 'input_folder' and 'output_folder' with your actual folder paths
input_folder = r'C:\Users\user\Desktop\raw-img\horse'
output_folder = r'C:\Users\user\Desktop\normalized\horse'

resize_images(input_folder, output_folder)
