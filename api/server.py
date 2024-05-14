import io
from flask import Flask, request, jsonify
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

# Load your Keras model and labels
model = load_model("../keras_Model.h5", compile=False)
class_names = open("../labels.txt", "r").readlines()

@app.route('/classify', methods=['POST'])
def classify_image():
    # Input Validation
    if 'image' not in request.files:
        return jsonify({"error": "No image file part"}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "No selected image file"}), 400
    
    # Image Preprocessing
    try:
        image = Image.open(io.BytesIO(image_file.read())).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        data[0] = normalized_image_array
    except Exception as e:
        return jsonify({"error": "Invalid image file or format"}), 400
        
    # Model Prediction
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Response
    return jsonify({"class": class_name[2:].strip(), "confidence": float(confidence_score)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
