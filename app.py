import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# ✅ Load your trained model
@st.cache_resource
def load_garbage_model():
    model = load_model("my_model.keras")   # <-- Updated here!
    return model

model = load_garbage_model()

# ✅ Label map — update if needed!
labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# ✅ Streamlit UI
st.title("♻️ Garbage Classification App")
st.write("Upload an image of garbage to classify it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # ✅ Preprocess
    img = image.resize((128, 128))
    x = img_to_array(img) / 255.0
    x = np.expand_dims(x, axis=0)

    # ✅ Predict
    preds = model.predict(x)
    pred_class = np.argmax(preds, axis=1)[0]
    confidence = preds[0][pred_class]

    st.write(f"**Prediction:** {labels[pred_class].capitalize()}")
    st.write(f"**Confidence:** {confidence:.2%}")
