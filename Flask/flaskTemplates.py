from flask import Flask, render_template

app = Flask(__name__)


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
