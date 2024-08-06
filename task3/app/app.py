from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from app.models.model import db


app = Flask(__name__)
app.config.from_object('config.DevelopementConfig')

csrf = CSRFProtect(app)

from app.registration.registration import registration

app.register_blueprint(registration, url_prefix='/registration' )


db.init_app(app)
@app.cli.command("init-db")
def init_db():
    # ошибка с неверным wsgi.py
    db.create_all()
    print('ok')

@app.route('/')
def index():
    return render_template('index.html')


if __name__=='__main__':
    app.run()