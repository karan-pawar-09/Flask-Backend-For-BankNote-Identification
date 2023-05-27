import os
from flask import Flask, request, jsonify
from keras.models import load_model
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.applications.resnet import ResNet50,preprocess_input
import numpy as np

print("start")

app = Flask(__name__)

# Load the Keras model
model = load_model('best_model.h5')

@app.route('/predict', methods=['POST'])

def predict():    
    # Get the file from the request
    file = request.files['file']
    filename = file.filename

    
    file.save("./uploads/" + filename);
    
    # Load the image and preprocess it
    img = load_img('uploads/' + filename, target_size=(256,256))
    
    img_ar = img_to_array(img)
    img_ar = preprocess_input(img_ar)
    img_ar = np.array([img_ar])

    # Make the prediction
    pred = model.predict(img_ar)[0]
    class_name = np.argmax(pred)

    # Return the predicted class name
    return jsonify({'class_name': str(class_name)})

if __name__ == '__main__':
    app.run(debug=True)

#  sudo curl -X POST -F 'image=@/Users/karan/AndroidStudioProjects/btechfinalproject/assets/1.png' http://127.0.0.1:5000/predict
