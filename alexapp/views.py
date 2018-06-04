from flask import Flask, render_template, request, current_app, Blueprint, redirect
from .models import Blogpost, db, Category, User
from .forms import LoginForm, NewPost
from flask_login import current_user, login_user

#Set the blueprint for this application to be blog
blog = Blueprint('blog', __name__, url_prefix='/blog')

#Route that takes the user to the dvelopments page
@blog.route('/blogposts')
def developments():
    query_test = Blogpost.query.all()
    return render_template('blog.html', developments=query_test)

@blog.route('/<category>')
def dev_details(category=None):
    #Commit seems to be required so that the query returns new results properly
    db.session.commit()
    #Query development table for the development specified in the uri
    category = Category.query.filter_by(name=category).first()
    #Grab the properties associated with the development from the uri
    posts = Blogpost.query.filter_by(category_id=category.id).all()
    return render_template('blog.html', category=category,
                           posts=posts)

@blog.route('/new', methods=['GET', 'POST'])
def new_dev():
    #Thi will take the information from the form and construct a development object
    #It will then add the object to the database using flask-sqlalchemy
    form = NewPost()
    if form.validate_on_submit():
        name = form.name.data
        details = form.details.data
        category = form.category.data
        db.session.add(Blogpost(name=name, details=details,
                                category=category))
        db.session.commit()
        return redirect('/')
    return render_template('new_post.html', form=form)

@blog.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('new'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username of password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('new'))
    return render_template('login.html', title='Sign In', form=form)
