# -*- coding:utf-8 -*-
# request Url 관련 속성
# path : url경로(환경 변수 PATH_INFO 와 같음)
# url : 전체 url 모두 표시
# base_url:  쿼리 스트링을 제외한 url 표시
# url_root : 환경변수 server_name과 같음


from flask import Flask,request

app = Flask(__name__)

@app.route('/example/envrion', methods=["GET","POST"])
def example():
    return("path : %s<br/>"
            "url: %s<br/> "
            "base_url: %s<br/>"
             "url_root: %s<br/>" )% (request.path,request.url,request.base_url,request.url_root)

if __name__ == '__main__':
    app.run()

