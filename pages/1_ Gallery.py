 
import streamlit as st
import os
from PIL import Image

# Set up the app title
st.title('Image Gallery')

# Folder containing images
IMAGE_FOLDER = 'images'

# List all images in the folder
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Display a message if no images are found
if not image_files:
    st.write("No images found in the directory.")
else:
    # Create a grid layout for images
    cols = st.columns(3)  # Adjust the number of columns as needed

    for i, image_file in enumerate(image_files):
        # Open and display the image
        image_path = os.path.join(IMAGE_FOLDER, image_file)
        image = Image.open(image_path)

        # Determine which column to display the image in
        with cols[i % len(cols)].container():
            st.image(image, caption=image_file, use_column_width=True)

