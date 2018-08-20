# -*- coding: utf-8 -*-
#request의 values 속성은 GET 또는 POST 메서드로 데이터를 보냈을 대
#   HTTP 메서드 타입에 상관없이 데이터를 읽어 올 수 있는 속성

#여기서 주의할 점은 GET 과 POST가 동일한 변수명을 사용했을 경우 values속성은 GET 메서드로
# 보낸 데이터를 우선으로 한다.
from flask import Flask, request

app = Flask(__name__)

@app.route('/abab',methods= ["GET","POST"])
def abab():
    #브라우저로 부터 변수가 넘어오지 않았을 경우에는 기본값을 설정할 수 있다.
    return request.values.get("name",default ="no data!!")

if __name__ =="__main__":
    app.run()

#http 메시지는 웹서버와 웹브라우저간의 문자열 타입으로만 테이터를 주고 받는다.
