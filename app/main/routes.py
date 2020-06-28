from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required
from app import db
from app.models import User, TrainingSession, Attendee
from app.main import bp
from app.main.forms import RegisterSession 
from datetime import datetime

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
        instructor = Trainin_session.query.filter_by(instructor=form.attendee.data)
        weapon_class = weapon_class
        date = date
        training = Training(date=date, attendee=attendee,)
        db.session.add(trainingtime)
        db.session.commit()
        flash('Your training session is now registered!')
        return redirect(url_for('main.index'))
    return render_template('main/index.html', title='Home', form=form)

###########################################################
# Redo index without PostForm just to see if I understand #
###########################################################
