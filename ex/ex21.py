# -*- coding:utf-8 -*-
# Response 객체에서 http 메서지 바디와 쿠키를 설정하는 메소드

# get_data : 브라우저에 응답할 데이터를 반환한다.(data 속성에 있는 값을 얻어온다.)
# set_data ; 브라우저에 응답할 데이터를 변경할 때 사용한다.
# set_cookie: 클라이언트 쿠키를 설정한다.

from flask  import  Flask,Response

app=Flask(__name__)

@app.route('/')
def res():
    res = Response("reponse test")

    res.set_data("flask study")
    return res

if __name__ == "__main__":
    app.run()
