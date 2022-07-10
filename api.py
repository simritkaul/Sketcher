from flask import Flask, render_template, request, redirect, flash
from main import *
import os

UPLOAD_FOLDER = os.path.join('static', 'images')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def getImage():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect('/')

        img = request.files['image']
        if img.filename == '':
            flash('No selected file')
            return redirect('/')

        if img and allowed_file(img.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
            img.save(path)
            sketch_image(path)
            os.remove(path)
            return render_template('result.html', sketchImage=os.path.join(app.config['UPLOAD_FOLDER'], 'sketch.png'))


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
