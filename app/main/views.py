from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required,current_user
from .forms import PitchesForm,CommentsForm,UpdateProfile
from ..models import Pitches,Comments,User
from .. import photos, db
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
    interview = Pitches.query.filter_by(category='Interview-Pitch').all()
    product = Pitches.query.filter_by(category='Product-Pitch').all()
    promotion = Pitches.query.filter_by(category='Promotion-Pitch').all()
    business = Pitches.query.filter_by(category='Business-Pitch').all()
    # pitches = Pitches.get_all_pitches()
    # promotion = Pitches.query.filter_by(category='Promotion-Pitch').all()
    # pitches = Pitches.query.all()
    # pitches = Pitches.query.order_by('-id').all()
    

    message= 'Welcome to the Pitches'
    # return "Hello, World"
    return render_template('home.html',title=title,message=message,interview=interview,product=product,promotion=promotion,business=business)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

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

        new_pitch = Pitches(body=body,category=category,user_id=current_user.id)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    return render_template('new_pitch.html', pitch_form = form)



@main.route('/pitch/<int:id>',methods = ['GET', 'POST'])
@login_required
def comment(id):

    comments_form = CommentsForm()
    # pitch = Pitches.query.get(pitch_id)
    pitches = Pitches.query.filter_by(id=id).first()
    print(pitches)
    if comments_form.validate_on_submit():
        comment = comments_form.comment.data

        new_comment = Comments(the_comment=comment,pitches_id=pitches.id, user_id = current_user.id)
        db.session.add(new_comment)
        db.session.commit()

    comments_list = Comments.query.filter_by(pitches_id=id).order_by("-id")
    print(comments_list)

    return render_template('comments.html', comments_form=comments_form,comments_list=comments_list)

# @main.route('/pitch/<int:id>/comments',methods = ['GET', 'POST'])
# @login_required
# def com_list(id):
#
#     # comments_form = CommentsForm()
#     # pitch = Pitches.query.get(pitch_id)
#     pitches = Pitches.query.filter_by(id=id).first()
#
#     # if comments_form.validate_on_submit():
#     #     comment = comments_form.comment.data
#     #
#     #     new_comment = Comments(the_comment=comment,pitches_id=pitches.id, user_id = current_user.id)
#     #     new_comment.save_comment()
#
#         # return redirect(url_for('main.home'))
#     comments_list = Comments.query.filter_by(pitches_id=pitches.id).all()
#
#     return render_template('com_list.html',comments_list=comments_list)



# @main.route('/comment/new',methods = ['GET', 'POST'])
# @login_required
# def comment():
#
#     comments_form = CommentsForm()
#     # pitch = Pitches.query.get(pitch_id)
#     # pitches = Pitches.query.filter_by(id=id).first()
#
#     if comments_form.validate_on_submit():
#         comment = comments_form.comment.data
#
#         new_comment = Comments(the_comment=comment, user_id = current_user.id)
#         new_comment.save_comment()
#
#         return redirect(url_for('main.home'))
#     # comments_list = Comments.query.filter_by(pitches_id=pitches.id).all()
#
#     return render_template('comments.html', comments_form=comments_form)


