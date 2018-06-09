########################################################
# DESCRIPTION:
# (import app decorator from __init__.py)
# sort queries and define different responses to them 
# work like a head file
#
# AUTHOR: ykx
# TIME: 2018.06.02
########################################################

#! /usr/bin/env python
# -*- coding:utf-8 -*-

from app import app # it means import the variable app from package app
from flask import request
from flask import render_template

###################

@app.route('/upload/')
def upload():
    return 



###################

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

if __name__ == '__main__':
    app.run()


########
# ref  #
########
# flask quickstart chinese: http://docs.jinkan.org/docs/flask/quickstart.html
# flask render_template: https://blog.csdn.net/bestallen/article/details/52055061
# flask quickstart: http://flask.pocoo.org/docs/1.0/quickstart/
# flask api: http://flask.pocoo.org/docs/1.0/api/#flask.Flask
# flask & download: https://www.cnblogs.com/we8fans/p/7107353.html
# flask & json: https://blog.csdn.net/matengbing/article/details/78653591
# flask & template: http://www.pythondoc.com/flask-mega-tutorial/templates.html
# flask request: https://www.cnblogs.com/wangjikun/p/6935592.html`

#Deployment Options: http://flask.pocoo.org/docs/1.0/deploying/#deployment
#Development Server: http://flask.pocoo.org/docs/1.0/server/#server
#url_for(): http://flask.pocoo.org/docs/1.0/api/#flask.url_for
