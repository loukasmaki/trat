from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from app import db
from app.models import User, TrainingSession, Attendee
from app.main import bp
from app.main.forms import RegisterSession 
from datetime import datetime
from sqlalchemy import and_

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
    print('creating form instance')
    form = RegisterSession() 
    print('validating on submit...')
    if form.validate_on_submit():
        print('In first IF statement')
        print ('Now checking if attendee already in database')
        attendee = Attendee.query.filter_by(name=form.attendee.data).first()
#        print('Checking instructor')
#        instructor = Attendee.query.filter_by(name=form.instructor.data).first_or_404()


        if attendee is None:
            print('In second if statement')
            attendee = Attendee(name=form.attendee.data)
            print('Trying add attendee to session')
            db.session.add(attendee)
        print('form vars')
        weapon_class = form.weapon_class.data
        date = form.date.data
#        training_session = TrainingSession.query.filter(
#            and_(TrainingSession.date == date, 
#                 TrainingSession.weapon_class == weapon_class)).first_or_404()

        query = db.session.query(TrainingSession).filter(
            TrainingSession.date == date,
            TrainingSession.weapon_class == weapon_class
        )
        training_session = TrainingSession()
        print(query)

        print('Done with vars')
        if query is None:
            print('in third if statement')
            training_session = TrainingSession(date=date, attendee=attendee, weapon_class=weapon_class, instructor=instructor.id)
        else:
            print('in else statement')
            training_session.date = date
            training_session.weapon_class = weapon_class
            training_session.set_instructor = form.instructor.data

        attendee.attending.append(training_session)

        print('adding to db session')

        db.session.add(training_session)
        db.session.commit()
        print("COmmited to db. Supposed to show flash and register pag again")
        flash('Your training session is now registered!')
        return redirect(url_for('main.index'))
    return render_template('main/index.html', title='Home', form=form)

