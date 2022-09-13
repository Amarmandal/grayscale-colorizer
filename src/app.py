from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SubmissionForm
import secrets
from PIL import Image
import urllib.request
import os
from werkzeug.utils import secure_filename
import shutil
from modelloader import use_model

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv(key='secret_key')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def save_picture(form_picture):
    picture_path = os.path.join(app.root_path, 'static/uploads/', form_picture.filename)
    output_size = (256,256)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return form_picture.filename

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Please select image for uploading. No image selected!!')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_picture(file)
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed as below:')
        use_model(filename)
        # shutil.copyfile(f"./static/uploads/{filename}",f"./static/outputs/{filename}")
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are: png, jpg and jpeg')
        return redirect(request.url)

@app.route('/display/input/<filename>')
def display_image_input(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/display/output/<filename>')
def display_image_output(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='outputs/' + filename), code=301)
