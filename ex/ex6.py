from flask import Flask,render_template

app= Flask(__name__)

@app.route('/')
def test_app():
    return render_template('layout2.html',title='Test',mybody='test page')


@app.route('/home')
def home():
    return render_template('layout2.html',title='home',mybody="main page")

@app.route('/about')
def about():
    return render_template('layout2.html',title="about",mybody="company introduce page")

@app.route('/contact')
def contact():
    return render_template('layout2.html',title='contact', mybody='mm page')

if __name__ == "__main__":
    app.run()


