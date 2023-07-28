
import time
import tensorflow as tf
from PIL import Image
import requests
from io import BytesIO
import numpy as np
from keras.models import load_model
import streamlit as st

st.title("Breast Cancer Image classification")

st.markdown("Model loaded using VGG16")

st.header("Please upload a mammogram")

st.caption("Choose an Image")

file = st.file_uploader("", type=['jped', 'jpg', 'png'])

model = load_model('')




st.subheader("Classifying.....")
with st.spinner("Wait for it...."):
    time.sleep(10)
    model = load_model()

classes = ["Benign", "Malignant"]

def scale(image):
    image = tf.cast(image, tf.float32)
    return tf.image.resize(image, [150, 150])

def decode_img(image):
    img = tf.image.decode_image(image)
    img = scale(img)
    return tf.expand_dims(img, axis=0)

# File Upload Input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image file and get its content
    image = uploaded_file.read()

    # Preprocess the image and get the prediction
    with st.spinner("Classifying..."):
        prediction = model.predict(decode_img(image))
        label = classes[prediction.argmax()]

    # Display the predicted class and the image
    st.write("Predicted class:", label)
    st.image(image, caption="Classifying Breast Cancer Image", use_column_width=True)
