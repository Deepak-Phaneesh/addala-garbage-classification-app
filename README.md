# 🗑️ Garbage Classification Web App

This is a simple **Streamlit web app** that uses a **TensorFlow deep learning model** to classify images of garbage into categories like cardboard, glass, metal, paper, plastic, or trash.

---

## 🚀 Features

- Upload an image of waste material
- Get a predicted category instantly
- Powered by a custom trained CNN model (`my_model.keras`)
- Clean, interactive UI built with Streamlit

---

## 📂 Project Structure

garbageClassification/
 ├── app.py               # Streamlit app script
 ├── my_model.keras       # Trained TensorFlow model
 ├── requirements.txt     # Python dependencies
 ├── .gitignore           # Files/folders to ignore in Git

---

## ⚙️ Requirements

- Python 3.10+
- TensorFlow
- Streamlit

Install all dependencies:
```
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Clone this repo:
```
git clone https://github.com/YOUR_USERNAME/garbage-classification-app.git
cd garbage-classification-app
```

2. (Optional but recommended) Create a virtual environment:
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the app:
```
streamlit run app.py
```

5. Open your browser at `http://localhost:8501`

---

## 🧠 How It Works

- The TensorFlow model (`my_model.keras`) was trained on a garbage classification dataset.
- The Streamlit app loads the model and runs predictions on uploaded images.
- The user gets an instant prediction in a clean web interface.

---

## 📜 License

This project is for learning and demonstration purposes only.
