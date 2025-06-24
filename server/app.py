from flask import Flask, request, jsonify
import os
from transcriber import transcribe_audio
from summarizer import summarize_text

app = Flask(__name__)
UPLOAD_FOLDER = "../uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    transcript = transcribe_audio(filepath)
    summary = summarize_text(transcript)

    return jsonify({"transcript": transcript, "summary": summary})

if __name__ == '__main__':
    app.run(debug=True)

