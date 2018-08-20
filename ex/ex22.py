from flask import Flask,Response

app=Flask(__name__)

@app.route('/')
def res():
    res = Response("flask study")
    res.set_cookie("id","flask study")

    return res

if __name__ == '__main__':
    app.run()

