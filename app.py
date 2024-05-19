# from flask import Flask, request, render_template, send_from_directory
# import os
# from PIL import Image
# from ultralytics import YOLO

# app = Flask(__name__)

# # Load your model
# model = YOLO('models/best.pt')

#UPLOAD_FOLDER = 'static/uploads/'
# RESULTS_FOLDER = 'static/results/'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULTS_FOLDER, exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('computer_vision.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return 'No file part'
    
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'

#     if file:
#         # Save the file to a temporary location
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         # Process the image with your YOLO model
#         results = model.predict(source=filepath)
        
#         # Extract the first result (assuming only one image is processed)
#         result_image_array = results[0].plot()  # This returns a numpy array
        
#         # Convert numpy array to PIL Image
#         result_image = Image.fromarray(result_image_array)

#         # Save the result image
#         result_image_path = os.path.join(RESULTS_FOLDER, file.filename)
#         result_image.save(result_image_path)
        
#         # Return the processed image path to the template
#         return render_template('result.html', image_filename=file.filename)

# @app.route('/uploads/<filename>')
# def send_uploaded_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)

# @app.route('/results/<filename>')
# def send_result_file(filename):
#     return send_from_directory(RESULTS_FOLDER, filename)

# if __name__ == '__main__':
#     app.run(debug=True, port=3000)

from flask import Flask, request, render_template, send_from_directory
import os
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)

# Load your model
model = YOLO('models/best.pt')

UPLOAD_FOLDER = 'static/uploads/'
RESULTS_FOLDER = 'static/results/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('computer_vision.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Save the file to a temporary location
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Process the image with your YOLO model
        results = model.predict(source=filepath)
        
        # Extract the first result (assuming only one image is processed)
        result_image_array = results[0].plot()  # This returns a numpy array
        
        # Convert numpy array to PIL Image
        result_image = Image.fromarray(result_image_array)

        # Save the result image
        result_image_path = os.path.join(RESULTS_FOLDER, file.filename)
        result_image.save(result_image_path)
        
        # Return the original and processed image paths to the template
        return render_template('result.html', original_filename=file.filename, processed_filename=file.filename)

@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/results/<filename>')
def send_result_file(filename):
    return send_from_directory(RESULTS_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
