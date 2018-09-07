from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    body = TextAreaField('Pitch Now',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on pitch',validators = [Required()])
    submit = SubmitField('Submit')

