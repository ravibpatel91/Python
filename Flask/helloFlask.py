from flask import Flask

app = Flask(__name__)


# Defining URL Route | Action Name
@app.route('/hello/', methods=['GET'])
def hello():
    return '<h1>Hello Flask</h1>'


# Passing parameters to a Route | Allowing type of HTTP Request (GET / POST)
@app.route('/home/<place>', methods=['GET', 'POST'])
def home(place):
    return '<h1>You are on ' + place + ' Home Page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
