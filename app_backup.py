from flask import Flask, request, jsonify
import face_recognition
import numpy as np
import os

app = Flask(__name__)

# Load known faces from the known_faces directory
def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir('known_faces'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join('known_faces', filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(filename.split('.')[0])  # Use filename without extension as name

    return known_face_encodings, known_face_names

known_face_encodings, known_face_names = load_known_faces()

@app.route('/match', methods=['POST'])
def match_face():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Save the uploaded file to the uploads folder
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Load the uploaded image and get face encodings
    uploaded_image = face_recognition.load_image_file(file_path)
    uploaded_face_encodings = face_recognition.face_encodings(uploaded_image)

    if len(uploaded_face_encodings) == 0:
        return jsonify({'error': 'No face found in the uploaded image'}), 400

    uploaded_face_encoding = uploaded_face_encodings[0]

    # Compare the uploaded face with known faces
    results = face_recognition.compare_faces(known_face_encodings, uploaded_face_encoding)

    # Check if there is a match
    if True in results:
        matched_index = results.index(True)
        matched_name = known_face_names[matched_index]
        return jsonify({'matched': True, 'name': matched_name}), 200
    else:
        return jsonify({'matched': False}), 200

if __name__ == '__main__':
    app.run(debug=True)
