# AI & Real Image Detector (DeepFake Classifier)

A web-based **image classification tool** built with **TensorFlow** and **Streamlit** to detect whether an image is **REAL** or **AI-generated (DeepFake)**. This application uses a pre-trained Convolutional Neural Network (CNN) model to analyze and classify images with high accuracy.


## 🚀 Features

- **Upload and Analyze Images**: Upload an image and instantly get predictions.
- **Fast & Accurate**: Detects AI-generated images (DeepFakes) with high confidence.
- **Web Interface**: Easy-to-use interface built with Streamlit.
- **AI-Powered**: Built on a TensorFlow model for accurate results.

---

## 🛠️ Tech Stack

- **TensorFlow**: Deep learning library for model training and inference.
- **Streamlit**: Web framework for creating data apps.
- **NumPy**: For numerical computing in Python.
- **Pillow**: For image processing and manipulation.

---

## 📦 Setup Instructions

### 🔧 Local Installation

1. **Clone the repository**  
   Clone this repo to your local machine:
   ```bash
   git clone https://github.com/Rahul2201020931/AI-Real-Image-Detector.git
   cd your-repo-name
   ```

2. **Install dependencies**  
   Install the necessary Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download or add the model**  
   The model is required for predictions. If not included in this repo, [download it from here](#) and place it inside the `model/` folder.

4. **Run the Streamlit app**  
   Launch the application:
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Information

- **Model File**: `AI_IMAGE_DETECTOR_full_model(DEEP).h5`
- **Input Size**: 32x32 pixels (RGB)
- **Output**: The model outputs a probability distribution for the two classes: 
  - `REAL` (Class 1)
  - `FAKE` (Class 0)

---

## 📂 Project Structure

```
.
├── app.py                  # Streamlit application for image upload and prediction
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignore unnecessary files
└── model/
    └── AI_IMAGE_DETECTOR_full_model(DEEP).h5  # Pre-trained model (if available)
```

---

## 🌐 Live Demo 

> You can also try the live version hosted on Hugging Face Spaces:
> [🔗 Try the app](https://huggingface.co/spaces/Rahul9898/ai)

---

## 🙌 Author

Created by [Rahul Kumar Gupta](https://github.com/Rahul2201020931)  
Made with ❤️ for AI research and DeepFake awareness.

---
