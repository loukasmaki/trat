from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from app import db
from app.models import User, TrainingSession, Attendee
from app.main import bp
from app.main.forms import RegisterSession 
from datetime import datetime

#Why did I uncomment this? :'D
#@bp.before_app_request
#def before_request():
#    if current_user.is_authenticated:
#        current_user.last_seen = datetime.utcnow()
#        db.session.commit()

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = RegisterSession() 
    if form.validate_on_submit():
        attendee = Attendee.query.filter_by(attendee=form.attendee.data).first_or_404()
        instructor = Attendee.query.filter_by(attendee=form.instructor.data).first_or_404()


        if attendee is None:
            attendee = Attendee(name=form.attendee.data)
            db.session.add(attendee)
# if the training sessions are in the database then I must search for them and add the data else create the entry in the database.
        weapon_class = form.weapon_class.data
        date = form.date.data
        training_session = TrainingSession.query.filter_by(date and weapon_class).first_or_404()
        if training_session is None:
            training_session = TrainingSession(date=date, attendee=attendee, weapon_class=weapon_class, instructor=instructor.id)
        else:
            training_session.date = date
            training_session.weapon_class = weapon_class
            training_session.instructor = instructor
            
        db.session.add(training_session)
        db.session.commit()
        flash('Your training session is now registered!')
        return redirect(url_for('main.index'))
    return render_template('main/index.html', title='Home', form=form)

