from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/pythondemo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Code Continue
#class Stories(db.app):

# Defining URL Route | Action Name
@app.route('/', methods=['GET'])
def index():
    return render_template('storyList.html')


# Defining URL Route | Action Name
@app.route('/newstory/', methods=['GET'])
def newstory():
    return render_template('createNewStory.html')


# Defining URL Route | Action Name
@app.route('/process/', methods=['POST'])
def processstory():
    storyTitle = request.form['inputStory']
    storyDesc = request.form['inputDescription']
    return render_template('storyList.html', storyTitle=storyTitle, storyDesc=storyDesc)


if __name__ == '__main__':
    app.run(debug=True)
