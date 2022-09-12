from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resource={r"/*": {'origins': "*"}})


# route
@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/teacherslogan', methods=['GET'])
def teacher_slogan():
    return "This is a message for teacher page from flask backend"


teachers = [
    {
        "id": uuid.uuid4().hex,
        "name": "Mr Li",
        "subject": "Math",
        "phone": "13613239788",
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Mr Wang",
        "subject": "EN",
        "phone": "13613237397",
    },
    {
        "id": uuid.uuid4().hex,
        "name": "Mr Ho",
        "subject": "Sports",
        "phone": "13391379173",
    },
]


# Add and fetch teacher
@app.route('/teachers', methods=['GET', 'POST'])
def add_or_fetch_teachers_info():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        teachers.append({
            "id": uuid.uuid4().hex,
            "name": post_data.get('name'),
            "subject": post_data.get('subject'),
            "phone": post_data.get('phone')}
        )
        response_object['message'] = post_data.get('name') + ' information added'
    else:
        response_object['teachers'] = teachers
    return jsonify(response_object)


# Del and Update teacher
@app.route('/teachers/<teacher_id>', methods=['PUT', 'DELETE'])
def del_or_update_teacher(teacher_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        del_teacher(teacher_id)
        teachers.append({
            "id": uuid.uuid4().hex,
            "name": post_data.get('name'),
            "subject": post_data.get('subject'),
            "phone": post_data.get('phone')}
        )
        response_object['message'] = post_data.get('name') + "Teacher Info Updated!"
    if request.method == "DELETE":
        del_teacher(teacher_id)
        response_object["message"] = "Successfully Deleted!"
    return jsonify(response_object)


def del_teacher(teacher_id):
    print(teacher_id)
    for t in teachers:
        if t.get("id") == teacher_id:
            teachers.remove(t)
            print(str(t) + "removed")
            return True


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8900)
