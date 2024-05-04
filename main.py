import streamlit as st
import os
import random
import time

def main():
    st.title("Image to Text Generator")
    st.write("**Study the image closely, you've got just 5 seconds to take it all in..")

    # Path to the images folder in the project directory
    images_folder = "images"

    # List the images in the images folder
    image_files = os.listdir(images_folder)

    # Display a button to generate a random image
    if st.button("Click here to Generate Image"):
        # Select a random image from the folder
        random_image_file = random.choice(image_files)
        random_image_path = os.path.join(images_folder, random_image_file)

        # Display the random image
        image_placeholder = st.empty()
        image_placeholder.image(random_image_path, use_column_width=True)

        # Display the count of seconds
        for i in range(5, 0, -1):
            st.write(f"Displaying image for {i} seconds...")
            time.sleep(1)

        # Clear the image placeholder and display 'Time's up'
        image_placeholder.empty()
        st.write("Time's up")

    st.write("---")
    st.write("**Click below to build an image using your words to recreate the above dipslayed image.")
    if st.button("Click here to build Image"):
        website_url = "https://designer.microsoft.com/image-creator"
        st.write(f'<iframe src="{website_url}" width=1000 height=950 style="border:none; margin-top:-470px;" sandbox="allow-scripts allow-same-origin" scrolling="no"></iframe>', unsafe_allow_html=True)

        # Button to return to the homepage
        if st.button("Return to Homepage"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
