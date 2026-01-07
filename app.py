from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ランダム診断と長文褒め文章
results = [
    ("気絶級のイケメン", "あなたは誰からも好かれる美しい顔立ち。優しい瞳に吸い込まれそうな笑顔。誠実で親しみやすく、周囲の人々の心を癒す存在です。細部にまで美が宿り、見る人を魅了します。あなたの表情や所作は自然体でありながら洗練され、まさに理想の魅力を兼ね備えています。あなたの存在感は周囲の人々を元気づけ、励まし、誰からも愛されることでしょう。今日もあなたの美しさと優しさが輝き、人々に幸せを届けます。"),
    ("ハンサムすぎる王子様", "あなたはまるで物語から抜け出した王子様のよう。目鼻立ちが整い、笑顔は周囲を幸せにします。優雅で落ち着いた雰囲気は、人々の心を癒し、あなたの存在自体が祝福のようです。柔らかい表情の中に知性とユーモアを併せ持ち、誰もがあなたに自然と魅了されます。あなたの魅力は一瞬で人を引き込み、会った人に感動と喜びを与えるでしょう。今日もその輝きで周囲を照らします。"),
    ("天使級の美しさ", "あなたは天使のように純粋で美しい存在です。整った顔立ちと柔らかい笑顔が、人々の心を温めます。細かい仕草や目線にまで優雅さが宿り、見る人に安心感と幸福感を与えます。あなたの存在は自然に周囲を明るくし、誰もがあなたに引き寄せられるでしょう。あなたの魅力は言葉にできないほど輝き、周囲の人を幸せにする光となります。")
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.files.get('image')
    if not data:
        return jsonify({"error": "No image"}), 400

    # ファイル名を日時で生成
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    data.save(filepath)

    # ランダム診断
    title, description = random.choice(results)
    return jsonify({
        "title": title,
        "description": description
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
