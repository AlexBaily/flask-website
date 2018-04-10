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

#Route that takes the user to the dvelopments page
@dev_blue.route('/developments')
def developments():
    query_test = Development.query.all()
    return render_template('developments.html', developments=query_test)

@dev_blue.route('/developments/<development>')
def dev_details(development=None):
    #Commit seems to be required so that the query returns new results properly
    db.session.commit()
    #Query development table for the development specified in the uri
    development = Development.query.filter_by(name=development).first()
    #Grab the properties associated with the development from the uri
    properties = Property.query.filter_by(development_id=development.id).all()
    return render_template('development.html', development=development,
                           properties=properties)

@dev_blue.route('/new', methods=['GET', 'POST'])
def new_dev():
    #Thi will take the information from the form and construct a development object
    #It will then add the object to the database using flask-sqlalchemy
    form = NewDevelopment()
    if form.validate_on_submit():
        name = form.name.data
        details = form.details.data
        db.session.add(Development(name=name, details=details))
        db.session.commit()
        return redirect('/dev/developments')
    return render_template('new_development.html', form=form)
