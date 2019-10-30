from flask import Flask

app = Flask(__name__)


# decorators (just like views) catch the url and rediect to function below
@app.route("/")
@app.route("/index")

# function called at index url
def index():
    return "<h1>Hello World!</h1>"