# -*- coding:utf-8 -*-
# app.config.from_object 메소드

from flask import *
import sqlite3

#sqlite 환경설정
DATABASE = 'my.db'
SECRET_KEY = 'development key'
USERNAME= 'root'
PASSWORD = '1234'

app = Flask(__name__)

# sqlite 환경 설정값을 읽어 오기
app.config.from_object(__name__)

# Request Hooking(HTTP 요청 전후의 처리)
# request 처리전에 데이터베이스 접속 및 테이블 생성이 필요하고,
# request 처리 후에는 데이터베이스 접속을 종료해야한다.

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def createTable(g):
    try:
        sql = 'create table if not exists student(name text, count int)'
        g.db.execute(sql)
        g.db.commit()
        print('create db')
    except Exception as err:
        print('error : ',err)


@app.before_request
def before_request():
    g.db = connect_db()
    createTable(g)
    print('before request')

@app.teardown_request
def teardown_request(exception):
    g.db.close()
    print('end request')

@app.route('/stu_insert')
def stu_insert():
    return render_template('stu_form.html')



@app.route('/ins' ,methods = ["POST"])
def insertData():
    result = "insert success"
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        try:
            sql = "INSERT INTO Student(name,count) VALUES(?,?)"
            data = (name,int(age))
            g.db.execute(sql,data)
            g.db.commit()
        except Exception as err:
            result = err

        return  result

@app.route('/select')
def select_stuData():
    try:
        sql = "SELECT * FROM Student"
        cur = g.db.execute(sql)
        data = cur.fetchall() # studata - > list[tuple]
        stuData = [dict(name = n,count =cnt) for n, cnt in data]
    except Exception as err:
        print('error : ', err)

    return render_template('view_stuData.html',stuData = stuData)

@app.route('/')
def myTest():
    return "hello flask!!! "



if __name__ == '__main__':
    app.run(debug=True)



