from flask import Flask, render_template, request, redirect, url_for, flash
from forms import SubmissionForm
import os
import secrets
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(key='secret_key')
app.config['UPLOAD_FOLDER'] = 'static/uploads'


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # f_name, f_ext = os.path.splitext(form_picture.filename)
    # picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/uploads/', form_picture.filename)
    output_size = (200,200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return form_picture.filename

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            # flash('Your image has been uploaded!', 'success')
            return redirect(url_for('index'))
    return render_template('index.html',form=form)