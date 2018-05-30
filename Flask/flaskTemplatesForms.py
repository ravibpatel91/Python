from flask import Flask, render_template, request

app = Flask(__name__)


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
