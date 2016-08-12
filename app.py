from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title="Home")

@app.route("/resume")
def render_resume():
    return render_template('resume.html', title="Resume")

@app.route("/introduction")
def render_introduction():
    return render_template('introduction.html', title="Introduction")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

