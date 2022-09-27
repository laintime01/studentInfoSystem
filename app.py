from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
# pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/sis_db"
db = SQLAlchemy(app)


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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table.columns}


app.config.from_object(__name__)

CORS(app, resource={r"/*": {'origins': "*"}})


# route
@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test', methods=['GET'])
def test_func():
    teachers_info = Teachers.query.all()
    return jsonify(teachers_info)


@app.route('/teacherslogan', methods=['GET'])
def teacher_slogan():
    return "This is a message for teacher page from flask backend"


# Add and fetch teacher
@app.route('/teachers', methods=['GET', 'POST'])
def add_or_fetch_teachers_info():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        new_teacher = Teachers(name=post_data.get('name'),
                               subject=post_data.get('subject'),
                               phone=post_data.get('phone'))
        db.session.add(new_teacher)
        db.session.commit()
        response_object['message'] = post_data.get('name') + ' information added'
    else:
        response_object['teachers'] = Teachers.query.all()
    return jsonify(response_object)


# Del and Update teacher
@app.route('/teachers/<teacher_id>', methods=['PUT', 'DELETE'])
def del_or_update_teacher(teacher_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        Teachers.query.filter(Teachers.id == teacher_id).update({
            'name': post_data.get('name'),
            'subject': post_data.get('subject'),
            'phone': post_data.get('phone')
        })
        db.session.commit()
        response_object['message'] = post_data.get('name') + "Teacher Info Updated!"
    if request.method == "DELETE":
        del_teacher(teacher_id)
        response_object["message"] = "Successfully Deleted!"
    return jsonify(response_object)


def del_teacher(teacher_id):
    print(teacher_id)
    d_teacher = Teachers.query.filter(Teachers.id == teacher_id).first()
    db.session.delete(d_teacher)
    db.session.commit()


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="localhost", port=8900)
