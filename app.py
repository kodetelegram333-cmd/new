from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({"error": "Rasm topilmadi"}), 400

    file = request.files['photo']
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"selfie_{timestamp}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Foydalanuvchini Google saytiga yo'naltirish
    return jsonify({"redirect": "https://www.google.com"})

if __name__ == "__main__":
    app.run(debug=True)
