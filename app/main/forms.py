from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required
from flask_wtf import FlaskForm


class MorseForm(FlaskForm):
    text = TextAreaField('Text', validators=[Required()])
    submit = SubmitField('Översätt')


class TextForm(FlaskForm):
    morse = TextAreaField('Morse', validators=[Required()])
    submit = SubmitField('Översätt')
