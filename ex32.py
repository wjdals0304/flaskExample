# -*- coding:utf-8 -*-
#메시지 플래싱 - 요청의 끝에 메시지를 기록하고 그 다음 요청에서만 그 메시지를 접근할 수 있또록 하는 기능

from flask import Flask, flash, redirect, render_template, request, url_for
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flash_login', methods=['GET', 'POST'])
def flash_login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'invalid password'
        else:
            flash('login success')
            return redirect(url_for('index'))

    return render_template('flash_login.html', error=error)


if __name__ == "__main__":
    app.run()