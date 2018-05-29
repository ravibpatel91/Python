from flask import Flask, render_template

app = Flask(__name__)

# Defining URL Route | Action Name
@app.route('/')
def index():
    return '<h1>Hello Flask</h1>'

# Passing parameters to a Route | Allowing type of HTTP Request (GET / POST)
@app.route('/home/<place>', methods=['GET', 'POST'])
def home(place):
    return '<h1>You are on ' + place + ' Home Page</h1>'

# Example of Templating
@app.route('/template/', methods=['GET'])
def template():
    return render_template('VariableTemplate.html', pageTitle='Google')


if __name__ == '__main__':
    app.run(debug=True)
