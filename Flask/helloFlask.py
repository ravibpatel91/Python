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
@app.route('/templateDefault/', methods=['GET'])
def templatedefault():
    return render_template('VariableTemplate.html')

# Example of Parameterized Templating
@app.route('/template/', methods=['GET'])
def template():
    titles = ['Title1', 'Title2', 'Title3', 'Title4', 'Title5']
    return render_template('VariableTemplate.html', pageTitle='Google', titles=titles)


if __name__ == '__main__':
    app.run(debug=True)
