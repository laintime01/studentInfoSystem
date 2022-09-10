from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resource={r"/*":{'origins':"*"}})


# route
@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/teacher', methods=['GET'])
def shark():
    return "This is a message for teacher from flask backend"


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=8900)
