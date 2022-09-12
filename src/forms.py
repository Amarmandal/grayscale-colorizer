from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, IntegerField, SubmitField, SelectField, DateField,
                     FileField, Label, TimeField, MultipleFileField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, NumberRange


class SubmissionForm(FlaskForm):
    # this is form for the submission of image
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Submit')