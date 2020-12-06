from flask import Flask

app = Flask(__name__)


@app.route("/")
def func_1():
    return "Hello world"


@app.route("/test")
def func_2():
    return "Test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
