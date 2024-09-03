from flask import Flask, request, jsonify, render_template
import os
from extractors.pdf_extractor import extract_form_fields
from extractors.ocr_extractor import extract_labels
from utils.text_processing import associate_labels_with_fields

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_pdf_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        json_output = extract_labels(file_path)
        os.remove(file_path)  # Clean up the uploaded file
        return json_output, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
