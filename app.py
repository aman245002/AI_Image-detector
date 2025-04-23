# app.py
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io
from PIL import Image

# Load model once at startup
@st.cache_resource
def load_trained_model():
    model_path = r"AI_IMAGE_DETECTOR_full_model(DEEP).h5"
    return load_model(model_path)

model = load_trained_model()

# Streamlit UI
st.title("AI Image Authenticity Detector")
st.write("Upload an image to check if it's REAL or FAKE.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image_pil = Image.open(uploaded_file)
    st.image(image_pil, caption='Uploaded Image', use_container_width=True)


    # Preprocess image
    img = image_pil.resize((32, 32))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred = model.predict(img_array)[0]
    class_idx = np.argmax(pred)
    label = "FAKE" if class_idx == 0 else "REAL"
    confidence = float(pred[class_idx])

    # Display results
    st.subheader("Prediction:")
    st.write(f"**Class**: {label}")
    st.write(f"**Confidence**: {confidence:.2f}")
