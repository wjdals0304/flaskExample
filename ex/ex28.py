# -*- coding:utf-8 -*-
# http 요청 전후에 대한 핸들러
# Flask 에서는 http 요청 전후에 사용할 수 있는 데코레이터를 제공하고 있다.

# before_first_request: 웹프로그램이 실행된 이후 가장 처음에 들어오는 http 요청에서만 실행
# before_request : 매번 HTTP 요청(request)이 들어올때 마다 실행
# after_request:  매번 http 요청이 끝나고 브라우저에 응답하기 전에 실행
# teardown_request : http 요청의 결과가 브라우저에 보내진 다음에 실행
# teardown_appcontext : http 요청이 완전히 완료되면  실행 (애플리케이션 컨텍스트 내에서 실행 )

from flask import Flask

app = Flask(__name__)

@app.route('/')
def res():
    return '/'

@app.before_first_request
def before_first_request():
    print("app first http request only")


@app.before_request
def before_request():
    print('http before')

@app.after_request
def after_request(response):
    print('http after')
    return response

@app.teardown_request
def teardown_request(exception):
    print('http result browser after')

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("http request's app context exit")

if __name__ == "__main__":
    app.run()









