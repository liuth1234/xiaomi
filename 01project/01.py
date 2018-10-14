from flask import Flask

app = Flask(__name__)


@app.route('/')
def index1():
    return "hello"

@app.route('/index')
def index2():
    return "python"
if __name__ == "__main__":
    app.run()
