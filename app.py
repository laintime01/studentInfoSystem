from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
# pip install flask-sqlalchemy
from model import db, Teachers, Students
import json
from getjson import GetJsonData

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/sis_db"
db.init_app(app)

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
    d_teacher = Teachers.query.filter(Teachers.id == teacher_id).first()
    db.session.delete(d_teacher)
    db.session.commit()


# Student controllers
@app.route('/studentslogan', methods=['GET'])
def get_student_slogan():
    return "Students information table"


@app.route('/students', methods=['GET', 'POST'])
def add_update_student():
    res_obj = {'status': 'success'}
    if request.method == 'POST':
        try:
            post_data = request.get_json()
            new_student = Students(name=post_data.get('name'),
                                   sex=post_data.get('sex'),
                                   age=post_data.get('age'),
                                   faculty=post_data.get('faculty'))
            db.session.add(new_student)
            db.session.commit()
            res_obj['message'] = post_data.get('name') + " added"
        except Exception as e:
            print(e)
    else:
        res_obj['students'] = Students.query.all()
    return jsonify(res_obj)


def del_student(student_id):
    d_student = Students.query.filter(Students.id == student_id).first()
    db.session.delete(d_student)
    db.session.commit()


@app.route('/students/<student_id>', methods=['PUT', 'DELETE'])
def update_del_student(student_id):
    res_obj = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        Students.query.filter(Students.id == student_id).update({
            'name': post_data.get('name'),
            'sex': post_data.get('sex'),
            'age': post_data.get('age'),
            'faculty': post_data.get('faculty'),
        })
        db.session.commit()
        res_obj['message'] = post_data.get('name') + "'s information updated!"
    else:
        del_student(student_id)
        res_obj['message'] = "info deleted!"
    return jsonify(res_obj)


# todolist
# write
@app.route('/todolist', methods=['POST'])
def test_write(path='todo.json', mode='a'):
    res_obj = {'status': 'success'}
    import _locale
    _locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])
    post_data = request.get_json()
    task = post_data.get('task')
    new_dict = {uuid.uuid4().hex: task}
    update_json = GetJsonData()
    update_json.json_update(new_dict)
    res_obj['message'] = "task added"
    return res_obj


# read
@app.route('/todolist', methods=['GET'])
def text_read(path='todo.json'):
    res_obj = {'status': 'success'}
    import _locale
    _locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])
    with open(path, 'r') as jf:
        jd = json.load(jf)
    res_obj['todolist'] = jd
    return jsonify(res_obj)


@app.route('/todolist/<task_key>', methods=['DELETE'])
def del_task(task_key):
    res_object = {'status': 'success'}
    delete_task = GetJsonData()
    delete_task.json_del(task_key)
    res_object['message'] = 'task done'
    return jsonify(res_object)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8900)
    with app.app_context():
        db.create_all()
