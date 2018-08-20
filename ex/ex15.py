# -*- coding:utf-8 -*-
#같은 변수에 여러개의 값이 넘어오는 경우에스는 리스트 타입으로 반환
# 이때 사용하는 메소드는 getlist메소드는 default 인자를 사용하지 않는다.

from flask  import Flask,request
from datetime import datetime

app= Flask(__name__)

class userDateType:
    def __init__(self,format):
        self.format=format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0],self.format)

@app.route("/eee",methods=["GET","POST"])
def eee():
    print(request.values.getlist("dates",type=userDateType("%Y-%m-%d")))
    return "console check!!."


if __name__ == "__main__":
    app.run()


