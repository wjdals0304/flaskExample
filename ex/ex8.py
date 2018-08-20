# -*- coding: utf-8 -*-
# 라우팅을 할 때 많이 사용하는 옵션 중에 redirect_to 옵션

from  flask import Flask

app = Flask(__name__)

@app.route('/aaa',redirect_to='/new_aaa')
def aaa():
    return "/aaa to page"

@app.route('/new_aaa')
def new_aaa():
    return '/new_aaa to page'

if __name__ == '__main__':
    app.run()

