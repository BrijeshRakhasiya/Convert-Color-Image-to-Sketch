import streamlit as st
import numpy as np
import imageio
import matplotlib.pyplot as plt
import scipy.ndimage
from PIL import Image
import io

# Function to convert image to sketch

def grayscaleimg(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def dodging(blur_img, gryscl_img):
    resultant_dodge=blur_img*255/(255-gryscl_img) 
    resultant_dodge[resultant_dodge>255]=255
    resultant_dodge[gryscl_img==255]=255
    return resultant_dodge.astype('uint8')

# Streamlit app
st.title('Image to Sketch Converter')

uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file).convert('RGB')
    img_array = np.array(image)

    # Convert to grayscale
    gryscl_img = grayscaleimg(img_array)

    # Invert image
    inv_img = 255 - gryscl_img

    # Blur image
    blurred_img = scipy.ndimage.gaussian_filter(inv_img, sigma=5)

    # Apply dodging
    target_img = dodging(blurred_img, gryscl_img)

    # Display sketch
    st.image(target_img, caption='Sketch Image', use_column_width=True, clamp=True)

    # Save sketch image to buffer
    buf = io.BytesIO()
    Image.fromarray(target_img).save(buf, format='PNG')
    byte_im = buf.getvalue()

    # Provide download button
    st.download_button(label='Download Sketch Image', data=byte_im, file_name='sketch.png', mime='image/png')
else:
    st.write('Please upload an image to convert it to a sketch.')

# Note: This code is to be run in a Streamlit environment.