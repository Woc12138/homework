from flask import make_response, Flask

app = Flask(__name__)


@app.route('/')
def set_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('Name', 'Hyman')
    return response

if __name__ == '__main__':
    app.run(debug=True)


