from flask import render_template, flash, redirect, url_for, request, g
from app import db
from app.models import User, Training_day, Attendee
from app.main import bp
from app.main.forms import RegisterSession 


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = RegisterSession() 
    if form.validate_on_submit():
        attendee = Attendee.query.filter_by(attendee=form.attendee.data).first_or_404()
        instructor = Trainin_session.query.filter_by(instructor=form.attendee.data)
        weapon_class = weapon_class
        date = date
        training = Training(date=date, attendee=attendee,)
        db.session.add(trainingtime)
        db.session.commit()
        flash('Your training session is now registered!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, attendee=attendee, weapon_class=weapon_class, date=date)

###########################################################
# Redo index without PostForm just to see if I understand #
###########################################################
