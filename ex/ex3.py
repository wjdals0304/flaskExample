# -*- coding: utf-8 -*-
# test_request_context() : flask에 있는 메소드이며, HTTP 요청을 테스트 할 수 있는 메소드
# url_for() 메소드 활용

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return '<h1>hello world!!</h1>'

@app.route('/user/<username>')
def get_user(username):
    return 'user: ' + username


if __name__ == '__main__':
    with app.test_request_context():
        print( url_for('hello'))
        print(url_for('get_user',username = 'kimkim'))


#웹프로그램 통신
#모든 웹프로그램은 사용자가 웹브라우저를 이용해서 웹프로그램이 가지고 있는 자원(상품정보,인강목록)
#요청하면 웹브라우저가 이해할 수 있는 형태로 재가공 하거나, 있는 자원 그대로 웹브라우저에게 반환해준다.
#웹 프로그램은 사용자가 보낸 요청과 요청을 처리한 결과를 웹서버를 경유해서 주고받는다
#이때 웹서버와 웹프로그램간의 메서지를 주고 받기 위한 약속이 필요한데 이약속을 CGI규약이라고 한다.
# CGI(common Gateway Interface);환경변수나 표준 입출력을 다룰 수있는 언어라면 모두 사용가능
# 실행속도나 개발 편의성을 고려하여 2000년대 초까지는 perl을 사용하였다.
# 소스코드의 보안성을 위해 c,c++, 델파이와 같은 언어를 사용하는 경우도 있는데, 이 언어들은
# 웹에 특화된 언어가 아니여서 유지보수나 프로그램 작성에 어려움이 있다.
# 파이썬은 cgi 모듈을 통해 CGI 환경변수와 CGI 표준 입출력에 직접 액세스해서 웹프로그램
#을 작성할 수 있다.  웹프로그램은 웹서버와는 독립적이어야 하는데 파이썬은 WSGI 표준을
#지켜 이독립성을 구현해준다.
# (WSG 표준을 따르면 웹서버의 종류와는 상관없이 동작이 된다.)

# FLASK는 Werkzeung(벡자이그) 기반으로 작성된다
# 벡자이그는 WSGI 코어와 URL 라우팅을 지원하고 있다.

