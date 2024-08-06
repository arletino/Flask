from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    id = db. Column(db.Integer, primary_key=True)
    user_first_name=db.Column(db.String(80), unique=False, nullable=False)
    user_second_name=db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(500), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), default=True, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return (f'User({self.user_first_name}, {self.user_second_name}, {self.email},{self.pwd_hash})')
    
    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)
          
    def check_password(self, password):
	    return check_password_hash(self.pwd_hash, password)

if __name__ == '__main__':
     db.create_all()