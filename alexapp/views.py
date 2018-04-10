from flask import Flask, render_template, request, current_app, Blueprint, redirect
from .models import Development, db, Property
from .forms import LoginForm, NewDevelopment
from flask_wtf import FlaskForm

#Set the blueprint for this application to be dev_blue
dev_blue = Blueprint('dev', __name__, url_prefix='/dev')

#Test route, routing is done via the dev_blue Blueprint
@dev_blue.route('/hello/<user>')
def hello_world(user=None):
    user = user or 'Alex'
    return render_template('index.html', user=user)

@dev_blue.route('/developments')
def developments():

    query_test = Development.query.all()
    return render_template('developments.html', developments=query_test)

@dev_blue.route('/developments/<development>')
def dev_details(development=None):

    db.session.commit()
    development = Development.query.filter_by(name=development).first()

    properties = Property.query.filter_by(development_id=development.id).all()

    return render_template('development.html', development=development,
                           properties=properties)

@dev_blue.route('/new', methods=['GET', 'POST'])
def new_dev():
    form = NewDevelopment()
    if form.validate_on_submit():
        name = form.name.data
        details = form.details.data

        db.session.add(Development(name=name, details=details))
        db.session.commit()

        return redirect('/dev/developments')

    return render_template('new_development.html', form=form)
