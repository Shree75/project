from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index3.html')


@app.route("/about")
def about():
    return render_template('index2.html')


@app.route("/contacts")
def contact():
    return render_template('index4.html')


if __name__ == '__main__':
    app.run(debug=True)
