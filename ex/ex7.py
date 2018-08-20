# -*- coding: utf-8 -*-
# # post 방식은 http 메서지의 body에 데이터를 포함해서 전달한다
# # 따라서 ,많은 양의 데이터를 전달 할때 사용하며 ,https 를 사용하는 웹서버는 전달하는 데이터가 중요하기 때문에 암호화 처리되어 전달
#
# @app.route('/aurl', methods =['GET'])
# def aaa():
#     pass
#
# @app.route('/aurl',methods=['POST'])
# def bbb():
#     pass
#
# #위의 코드는 http메소드 타입에 따라 뷰함수가 다른 경우
#
# #아래의 코드는 http 메도드 타입이 다르더라도 하나의 뷰함수 사용
# @app.route('burl',methods=['GET','POST'])
# def ccc():
#     pass
#
# # rounte 데코레이터에 methods 인자가 없으면 뷰함수는 GET요청만을 처리하게된다 ..
#
# # URL 변수에 기본값 할당하기
#
# @app.route('/aaa',defaults={'page':'index'})
# @app.route('/aaa/<page>')
#
# # 브라우저에서 /aaa/ 를 호춯한 경우에는 /aaa/index 형태의 주소를 호출한 것과 같다  .

from flask import Flask

app= Flask(__name__)

@app.route('/aaa',defaults={'bbs_id':100})
@app.route('/aaa/<bbs_id>')
def aaa(bbs_id):
    return "aaa의 {}번 글 입니다.".format(bbs_id)

if __name__ == '__main__':
    app.run()











