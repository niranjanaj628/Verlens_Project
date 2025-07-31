from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
model = tf.keras.models.load_model('model/deepfake_detector.keras')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    img_path = os.path.join(upload_dir, filename)
    file.save(img_path)

    try:
        # Preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = preprocess_input(img_array)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict using your model
        prediction = model.predict(img_array)[0][0]
        confidence = float(prediction)
        label = "Fake" if confidence >= 0.5 else "Real"
        confidence_pct = confidence if label == "Fake" else 1 - confidence
        
        confidence = float(prediction)

        if confidence >= 0.5:
            label = "Fake"
            confidence_pct = confidence * 100
        else:
            label = "Real"
            confidence_pct = (1 - confidence) * 100


        return jsonify({
            'result': label.lower(),
            'confidence': round(confidence_pct, 2)
        })

    except Exception as e:
        return jsonify({'error': f'Exception during prediction: {str(e)}'}), 500

    finally:
        # Clean up saved image
        if os.path.exists(img_path):
            os.remove(img_path)

if __name__ == '__main__':
    app.run(port=5000)
