from flask import *
app = Flask(__name__)


@app.route('/')
def hello():
 return "<h1>Welcome to Geeks for Geeks</h1>"
if __name__ == '__main__':
    app.run()
