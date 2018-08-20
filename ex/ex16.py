# -*- coding:utf-8 -*-
# MultiDict 데이터 타입 : get 과 post 메서드로 넘어온 데이터 (키,값) 튜플형태의 리스트 타입
# MultiDict 타입에서 제공하는 메서드
#get,getlist,add,setlist,clear,copy,deepcopy,pop,poplist

#add: MultiDict에 키와 값을 추가하는 메소드
#setfault : add 메소드와 거의 비슷하게 동작하지만, 변수가 있을 때는 그 변수의 값을 리턴
#           설정하고자 하는 변수가 없을 때 default값으로 데이터를 추가한다.

# copy(얕은복사) : MultiDict 데이터의 변수값이 있는 리스트 타입으로 있는 경우 그 리스트 타입의 메모리주소를
#                 복사
#deepcopy(깊은복사) : 리스트 타입의 메모리 주소가 아니라, 그 데이터를 복사

#pop : get메소드와 유사한 동작을 하지만 가능적인 차이가 있다. get메소드는 multiDict 데이터변수에서
#      특정 변수 키의 키값을 메모리에서 복사해서 프로그램에 리턴을 하는 반면에,
#      pop은 변수 키의 값을 복사하는 것이 아니라 multiDict 데이터 변수에서 변수 키를 제거하고 그값을 리턴한다.

#poplist: pop 메소드와 같은 동작을 하지만 같은 이름의 변수 키로 여러 값이 들어올 때 이 값들을 꺼내올 때
#        사용한다. getlist와의 차이점은 꺼내온 뒤에 기존의 MultiDict 변수의 키를 제거한다.

# envrion 사전에서 제공하는 표준 환경 변수
#  request_method : 웹브라우저가 보낸 요청의 처리 방식에 대한 문자열 포함

# script_name : 스크립트 파일명을 표현, Flask에서는 빈값으로 출력

# PATH_INFO: URL 경로(PATH),  예> http://www.aaa.com/ccc/main --> /ccc/main

#content_type: 웹브라우저가 보낸 http 요청 메시지의 바디에 포함되는 콘텐츠 형태 저장
#              HTTP헤더에 Content-type헤더 값을 확인한다.

# SERVER_NAME: 서버의 도메인 주소(IP)가 저장 , 예> http://www.aaa.com/ccc/main  --> www.aaa.com

# SERVER_PORT: 웹 어플리케이션이 동작하고 있는 서버 포트번호가 저장
# 예) Http://www.aaa.com:5000/env -->  5000 저장 , 도메인주소에 포트가 없으면 80
# SERVER_PROTOCOL : 웹 어플리케이션이 동작하는 서버 프로토콜 버전이 표시, HTTP/1.1
# QUERY_STRING:URL 끝에 보면 ?문자 뒤에 오는 문자열을 쿼리 스트링이라고 한다. 키 =값의 형태로 지정
#  키 값이 두개 이상일 때는 키 사이에 &문자로 구분한다.
# request의 environ 속성 : http 통신에 사용하는 환경 변수를 담고 있는 사전

#<wsgi 전용 환경 변수 >
# wsgi.version :WSGI 버전을 튜플 형태로 반환 (1.0)
# wsgi.url_scheme: URL 스키마의 종류,웹서버인 경우에는 HTTP를 반환한다.

from flask import Flask,request

app = Flask(__name__)

@app.route("/test/environ",methods = ["GET","POST"])
def test():
    strVal = ("REQUEST_METHOD : %(REQUEST_METHOD)s<br/>"
              "PATH_INFO : %(PATH_INFO)s<br/>"
              "QUERY_STRING : %(QUERY_STRING)s<br/>"
              # "CONTENT_TYPE: %(CONTENT_TYPE)s<br/> "
              "SERVER_NAME: %(SERVER_NAME)s<br/>"
              "SERVER_PORT: %(SERVER_PORT)s<br/>"
              "SERVER_PROTOCOL: %(SERVER_PROTOCOL)s<br/>"
              "wsgi.version: %(wsgi.version)s<br/>"
              "wsgi.url.scheme: %(wsgi.url_scheme)s ") % request.environ
    return strVal

if __name__ == "__main__":
    app.run()







