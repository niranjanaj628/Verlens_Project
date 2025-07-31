import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image

# Build absolute path to model
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, "model", "deepfake_detector.keras")

# Load model
model = tf.keras.models.load_model(model_path)

# Function to preprocess and predict an image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)  # shape: (1, 224, 224, 3)

    # prediction = model.predict(img_array)[0][0]  # Get scalar value
    # confidence = float(prediction) if prediction > 0.5 else 1 - float(prediction)
    # label = "Real" if prediction > 0.5 else "Fake"
    # confidence = float(prediction) * 100 if label == "Real" else (1 - float(prediction)) * 100
    # return {
    #     "label": label,
    #     "confidence": round(confidence * 100, 2)
    # }
    
    prediction = model.predict(img_array)[0][0]  # Scalar value between 0 and 1

    if prediction > 0.5:
        label = "Fake"
        confidence = prediction  # How confident it is that it's fake
    else:
        label = "Real"
        confidence = 1 - prediction  # How confident it is that it's real

    confidence = round(confidence * 100, 2)

    return {
    "label": label,
    "confidence": confidence
}



# Example usage (replace with actual uploaded image path)
if __name__ == "__main__":
    test_img_path = os.path.join(base_dir, "test", "sample.jfif")  # Make sure this file exists
    result = predict_image(test_img_path)
    print(f"Prediction: {result['label']} ({result['confidence']}% confidence)")
