from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SubmissionForm
import secrets
from PIL import Image
import urllib.request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(key='secret_key')
app.config['UPLOAD_FOLDER'] = 'static/uploads'


# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     # f_name, f_ext = os.path.splitext(form_picture.filename)
#     # picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/uploads/', form_picture.filename)
#     output_size = (200,200)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)
#     return form_picture.filename

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = SubmissionForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             picture_file = save_picture(form.image.data)
#             # flash('Your image has been uploaded!', 'success')
#             return redirect(url_for('index'))
#     return render_template('index.html',form=form)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

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
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
		return render_template('index.html', filename=filename)
	else:
		flash('Allowed image types are - png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/input/<filename>')
def display_image_input(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/display/output/<filename>')
def display_image_output(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='output/' + filename), code=301)