from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()


# create table teacher
# Python 3.7+ and Flask 1.1+ can use the built-in dataclasses package
@dataclass
class Teachers(db.Model):
    # table name
    __tablename__ = 'teacher'
    id: int
    name: str
    subject: str
    phone: str

    # column
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))


@dataclass
class Students(db.Model):
    __tablename__ = 'students'
    id: int
    name: str
    sex: str
    age: int
    faculty: str

    # column
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    sex = db.Column(db.String(20))
    age = db.Column(db.Integer)

    def __init__(self, name=None, faculty=None, sex=None, age=None):
        self.name = name
        self.faculty = faculty
        self.sex = sex
        self.age = age


@dataclass
class Users(db.Model):
    __tablename__ = 'users'
    id: int
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Student %r>' % (self.name, self.faculty, self.sex, self.age)
