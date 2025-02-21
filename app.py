from flask import Flask
from flask_cors import CORS
from routes.week_one import week_one_bp

app = Flask(__name__)
app.register_blueprint(week_one_bp)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
