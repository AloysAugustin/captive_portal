#!/usr/bin/env python

from flask import Flask, request, redirect, render_template
import urllib
import os

app = Flask(__name__)

def login_user(ip):
    os.system("sudo iptables -I internet 1 -t mangle -s " + ip + " -j RETURN")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'login' in request.form and 'password' in request.form:
        print 'login:', request.form['login'], 'password:', request.form['password']
        login_user(request.remote_addr)
        if 'orig_url' in request.args and len(request.args['orig_url']) > 0:
            return redirect(urllib.unquote(request.args['orig_url']))
        else:
            return render_template('login_successful.html')
    else:
        return render_template('login.html', orig_url=urllib.urlencode({'orig_url': request.args.get('orig_url', '')}))

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("http://10.20.0.1/login?" + urllib.urlencode({'orig_url': request.url}))

if __name__ == "__main__":
#    app.debug = True
    app.run('0.0.0.0', port=80)

