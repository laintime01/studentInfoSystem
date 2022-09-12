from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resource={r"/*":{'origins':"*"}})


# route
@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/teacherslogan', methods=['GET'])
def teacher_slogan():
    return "This is a message for teacher page from flask backend"


teachers = [
    {
        "id": "10000",
        "name": "Mr Li",
        "subject": "Math",
        "Phone": "13613239788",
    },
    {
        "id": "10001",
        "name": "Mr Wang",
        "subject": "EN",
        "Phone": "13613237397",
    },
    {
        "id": "10002",
        "name": "Mr Ho",
        "subject": "Sports",
        "Phone": "13391379173",
    },
]


@app.route('/teachers', methods=['GET', 'POST'])
def handle_teachers_info():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        teachers.append({
            "id" : post_data.get('id'),
            "name":post_data.get('name'),
            "subject":post_data.get('subject'),
            "phone":post_data.get('phone')}
        )
        response_object['message'] = post_data.get('name') + ' information added'
    else:
        response_object['teachers'] = teachers
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8900)
