# -*- coding:utf-8 -*-
# 사용자 정의 타입이 클래스인 경우
# get 메소드에서 datetime 객체 사용하기 위해서는 __call__ 메소드를 정의


from flask import Flask,request
from datetime import datetime

app = Flask(__name__)

class userDateType:
    def __init__(self,format):
        self.format = format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0],self.format)

@app.route("/ddd",methods=['GET','POST'])
def ddd():
    print(request.values.get("date","2015-05-25",type=userDateType("%Y-%m-%d")))
    return "console check"


if __name__ == "__main__":
    app.run()