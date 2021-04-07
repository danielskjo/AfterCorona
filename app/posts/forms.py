from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    place = StringField('Place', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create Post')