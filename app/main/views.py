from flask import render_template,request
from . import main
from flask_login import login_required,current_user
# from ..requests import get_sources_by_cat,get_all_articles,get_headline_articles
# from ..models import Source,Article


@main.route('/')
def index():

    '''
    View root page function that returns the general news sources by category
    '''
    # message = "Hello World"
    title="Pitches"

    message= 'Welcome to the Pitches'
    # return "Hello, World"
    return render_template('home.html',title=title,message=message)

