from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class NewPost(FlaskForm):
    name = StringField('Blog Post Name', validators=[DataRequired()])
    details = StringField('Details')
    category = StringField('Category')
    submit = SubmitField('Add new')
