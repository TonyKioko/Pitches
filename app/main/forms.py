from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PitchesForm(FlaskForm):
    category = SelectField('Pitch Category',
                              choices=[('Select','Select Category'), ('Interview-Pitch', 'Interview Pitch'), ('Product-Pitch', 'Product Pitch'),
                                       ('Promotion-Pitch', 'Promotion Pitch'), ('Business-Pitch', 'Business Pitch')], validators=[Required()])
    body = TextAreaField('Pitch Now',validators = [Required()])
    submit = SubmitField('Submit')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on pitch',validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


