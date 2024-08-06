import sys
from flask import (
    Blueprint, 
    request, 
    redirect, 
    render_template, 
    url_for, 
    flash
)
from app.models.form import RegisterForm
from app.models.model import User
from app.app import csrf, db


registration = Blueprint('registration', 
                         __name__, template_folder='templates', 
                         static_folder='static'
                         )

@registration.route('/')
def index():
    return render_template('registration/index.html')

@registration.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def form():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate():
            if user_is_exist(request.form['email']):
                return 'User with such email is exists'
            try:
                user = User(
                    user_first_name=request.form['firstname'], 
                    user_second_name=request.form['secondname'], 
                    email=request.form['email'],  
                )
                user.set_password(request.form['password'])
                db.session.add(user)
                db.session.flush()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return 'Registration is wrong'
        return 'Registration is ok'
    return render_template('registration/register_form.html', form=form)

def user_is_exist(user_email):
    return not User.query.filter_by(email = user_email).all() is None



