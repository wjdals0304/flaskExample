# -*- coding:utf-8 -*-
# 쿠키는 기본적으로 쿠키 이름과 쿠키 값으로 구성
# 쿠키는 정해진 시간동안 유지된다.
# 쿠키는 지정된 웹사이트의 경로에 영향을 미친다.
# 쿠키는 지정된 도메인 주소에 영향을 미친다.

# set_cookie 인자
#key: 쿠키 이름 (쿠키를 설정할 때는 반드시 이름을 지정해야한다 .
#value : 쿠키 값 기본값은 빈 문자열
#max_age : 쿠키 지속시간. 기본값은 None인데 None이면 브라우저가 닫힐 때 자동으로 쿠기가 제거된다.
#           시간 단위는 초단위의 시간값을 전달한다. 시간설정되면 초단위의 시간이 지나면 해당쿠키가 삭제된다.

# domain : 쿠키의 영향력이 미치는 도메인 주소 . 기본값은 None 이다.
# path: 쿠키의 영향력이 미치는 웹사이트의 경로 , 기본값은 "/" 이다.

# 쿠키 생성 / 삭제 / 확인
from flask import Flask,request, Response

app=Flask(__name__)

@app.route("/cookie_set")
def cookieSet():
    res = Response("Cookie create")
    res.set_cookie("cname","flask study")
    return  res

@app.route("/cookie_out")
def cout():
    res = Response("Cookie remove")
    res.set_cookie("cname",expires=0)
    return res

@app.route("/cookie_status")
def cstatus():
    return "cname cookie is %s" % request.cookies.get('cname','')

if __name__ == "__main__":
    app.run()
