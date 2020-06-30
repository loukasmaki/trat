from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from app import db
from app.models import User, TrainingSession, Attendee
from app.main import bp
from app.main.forms import RegisterSession 
from datetime import datetime
from sqlalchemy import and_
import datetime
from datetime import timedelta

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
        attendee = Attendee.query.filter_by(name=form.attendee.data).first()
        # Still need to implement instructor check
#        print('Checking instructor')
#        instructor = Attendee.query.filter_by(name=form.instructor.data).first_or_404()
#        put a pin in that until I have decided how training sessions gets defined. 
        query = db.session.query(Attendee).filter(
            Attendee.name == form.instructor.data,
            Attendee.instructor == True)


        if attendee is None:
            attendee = Attendee(name=form.attendee.data)
            db.session.add(attendee)

        weapon_class = form.weapon_class.data

        date = form.date.data
        today = date.today()

        if date > today:
            flash('Can\'t register a date in the future')

            return redirect(url_for('main.index'))


        if date > today:
            pass
#        training_session = TrainingSession.query.filter(
#            and_(TrainingSession.date == date, 
#                 TrainingSession.weapon_class == weapon_class)).first_or_404()

        query = db.session.query(TrainingSession).filter(
            TrainingSession.date == date,
            TrainingSession.weapon_class == weapon_class
        )
        training_session = TrainingSession()

        if query is None:
            training_session = TrainingSession(date=date, attendee=attendee, weapon_class=weapon_class, instructor=instructor.id)
        else:
            training_session.date = date
            training_session.weapon_class = weapon_class
            training_session.set_instructor = form.instructor.data

        attendee.attending.append(training_session)


        db.session.add(training_session)
        db.session.commit()
        flash('Your training session is now registered!')
        return redirect(url_for('main.index'))
    registered_attendees = Attendee.query.filter(Attende.name == form.attendee.data, )

    return render_template('main/index.html', title='Home', form=form, registered_attendees=registered_attendees.items)

@bp.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    # Admin view is for assigning instructors
    # Adding and changing schedule

    attendees = Attendee.query.order_by()

