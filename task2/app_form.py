from flask import (
    Flask,
    flash, 
    request, 
    make_response, 
    render_template, 
    url_for, 
    redirect,
    session
) 
    
import secrets
import sys


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()

@app.route('/', methods=['GET', 'POST'])
def index():
    url_btn = url_for('page_form')
    btn_name = "Enter"
    if  context:= {**request.cookies}:
        context.pop('session', None)
        url_btn = url_for('del_cookie')
        btn_name = 'Exit'   
    return render_template('index.html', url_entry=url_btn, msg='', btn_name=btn_name, context=context)


@app.route('/form')
def page_form():
    f = [
        {'name': "Name", 'type': 'text'}, 
        {'name': "e-mail", 'type': 'text'}
    ]
    return render_template('form.html', fields=f)


@app.route('/set_cookie', methods=['GET', 'POST'])
def set_cookie():
    response = make_response(redirect(url_for('index')))
    if request.method == 'POST':
        if not(''.join(list(request.form.values()))):
            flash("fields can't be empty")
            return redirect(url_for('page_form'))
        session['Name'] = request.form.get('Name')
        for key, value in request.form.items():
            response.set_cookie(key, value)
    return response

@app.route('/del_cookie')
def del_cookie():
    response = make_response(redirect(url_for('index')))
    session.pop('Name', None)
    for key, value in request.cookies.items():
        response.set_cookie(key, value, max_age=0)
    return response   

if __name__== '__main__':
    app.run(debug=True)