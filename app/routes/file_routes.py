import os
from flask import Blueprint, request, jsonify, send_from_directory, current_app

file_bp = Blueprint('file_bp', __name__)

# Upload file endpoint
@file_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully'}), 201

# List uploaded files
@file_bp.route('/', methods=['GET'])
def list_files():
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files})

# Download file by name
@file_bp.route('/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
