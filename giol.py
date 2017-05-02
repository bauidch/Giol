from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)