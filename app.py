from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    result_text = None
    if request.method == "POST":
        file = request.files.get("photo")
        if file:
            filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            image_url = url_for('uploaded_file', filename=filename)
            result_text = "顔診断結果: あなたは素晴らしい顔立ちです！"  # 固定テキスト

    return render_template("index.html", image_url=image_url, result_text=result_text)

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return redirect(url_for('static', filename=f"uploads/{filename}"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
