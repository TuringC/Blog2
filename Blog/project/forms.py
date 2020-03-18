from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class CommentInput(FlaskForm):
    body = TextAreaField(validators=[DataRequired()], render_kw={'class':"form-control", 'rows':"3", 'placeholder':'Leave a comment here...'})
    submit =SubmitField(render_kw={'class':'btn btn-light'})

class ArticleInput(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(1, 30)], render_kw={'class':"form-control"})
    body = TextAreaField('Article', validators=[DataRequired()], render_kw={'class':"form-control", 'rows':"8", 'placeholder':'Write your new blog here...'})
    submit = SubmitField(render_kw={'class':'btn btn-light'})

class LoginForm(FlaskForm):
    username = StringField('', validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder":"Username", "type":"text", "class":"form-control text-center"})
    password = PasswordField('', validators=[DataRequired(), Length(1, 16)], render_kw={"placeholder":"Password", "type":"password", "class":"form-control text-center"})
    submit = SubmitField('Go', render_kw={"class":"btn btn--icon login__block__btn", })

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete', render_kw={'class':'btn btn-light'})