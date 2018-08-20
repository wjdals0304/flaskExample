# -*- coding: utf-8 -*-

from flask import Flask, render_template
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/')
def temp_test():
    return render_template("super.html",my_string="테스트"
                            ,my_list = [11,22,33,44,55,66,77] )

if __name__ == "__main__":
    app.run(debug=True)


#템플릿 상속
#{% extends "<부모 템플릿의 이름 >" %},
#{% block %}<대체팔 코드>{% endblock %}