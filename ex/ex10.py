# -*- coding: utf-8 -*-
# HTTP 메시지( request 메시지, response 메시지)
# HTTP 메시지는 평문 형태로 되어 있으며,논리적인 구분으로 헤더와 바디로 구분
# 이때 헤더와 바디의 구분은 빈줄로 구분한다.

#Flask에서 http 요청과 응답을 처리하기 위해서는 request 객체와 response객체

#flask 모듈에서 request 클래스를 가져온다.

from flask import Flask,request
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

# Get방식에서 넘어온 변수값 가져오기
@app.route('/aaa')
def aaa():
    return "request 객체를 이용한 변수 name 값은 {} 입니다.".format(request.args.get('name'))


if __name__ == "__main__":
    app.run()
#request.args 에서 args는 get방식으로 전달된 데이터만 접근할 수 있다.


