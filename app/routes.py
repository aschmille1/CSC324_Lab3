from app import app
from flask import render_template
from app.forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'aschmille'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'SEC300', 'title': 'Intro to Cybersecurity'},'instructor': 'Yipkei Kwok'},
               {'classInfo': {'code': 'CSC386', 'title': 'Operating Systems Concepts'}, 'instructor': 'Yipkei Kwok'},
               {'classInfo': {'code': 'CSC208', 'title': 'Discrete Structures I'},'instructor': 'Baoqiang Yan'}]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

