from flask import render_template, flash, redirect, url_for, request, g
from app import app, db
from app.models import Uset, Training


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        training = Training(date=date, attendee=attendee,)
        db.session.add(trainingtime)
        db.session.commit()
        flash('Your training session is now registered!')
        return redirect(url_for('index'))

###########################################################
# Redo index without PostForm just to see if I understand #
###########################################################
