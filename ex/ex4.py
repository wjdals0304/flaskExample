from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>hello world!!</h1>'

@app.route('/user/<username>')
def user(username):
    return render_template('aa.html',name=username)

if __name__ == '__main__':
    app.run()


#jinja2에서 템플릿 표현식

# {%: block_start_string,  %} :block_end_string( 템플릿에서의 프로그래밍 영역을 넣기 위한 기호 )
# {{ : 변수를 출력하기 위해 시작하는 기호 : variable_start_string
# }} : 변수 출력이 끝나고 나서 사용하는 기호 : variable_end_string
# {# : 주석을 넣기 위해 시작하는 기호 - comment_start_string , #} 주석을 넣고 종료하기 위해 사용하는 기호 comment_end_string

