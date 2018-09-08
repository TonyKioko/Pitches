from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user
from .forms import PitchesForm,CommentsForm
from ..models import Pitches,User
from .. import db
from datetime import datetime

# from ..requests import get_sources_by_cat,get_all_articles,get_headline_articles
# from ..models import Source,Article

# @main.template_filter('datetimeformat')
# def datetimeformat(value,format='%B'):
#     return value.strftime(format)

@main.route('/')
def home():

    '''
    View root page function that returns the general news sources by category
    '''
    # message = "Hello World"
    title="Pitches"
    # pitches = Pitches.query.all()
    # pitches = Pitches.query.order_by('-id').all()
    pitches = Pitches.get_all_pitches()

    message= 'Welcome to the Pitches'
    # return "Hello, World"
    return render_template('home.html',pitches=pitches,title=title,message=message)

@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = PitchesForm()

    if form.validate_on_submit() and form.category.data != 'Select':
        body = form.body.data
        category = form.category.data

        new_pitch = Pitches(body=body,category=category)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    return render_template('new_pitch.html', pitch_form = form)

