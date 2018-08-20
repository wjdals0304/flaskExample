# -*- coding:utf-8 -*-
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/login',methods = ['GET','POST'])
def login():
     if request.method == 'GET':
         return render_template('test_login.html')
     else:
         userEmail=request.form['email']
         userPw = request.form['pw']
         return 'email : '  + userEmail + '  pw : ' + str(userPw)

if __name__ == "__main__":
    app.debug = True
    app.run()




