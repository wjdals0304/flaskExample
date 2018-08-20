# -*- coding:utf-8 -*-
# response를 json으로 만들기

from flask import Flask,jsonify

app = Flask(__name__)

work = [
    {'id' : 100,
     'title': 'food purchase',
     'description' : 'milk,cheeze,pizza',
     'done' : False},
    {
    'id': 200,
    'title' : 'flaks practice',
    'description': 'web programming',
    'done' : False
    }
]

@app.route('/json',methods=['GET'])
def get_works():
    return jsonify(work)

if __name__ =="__main__":
    app.run()