from flask import Flask, request

app = Flask(__name__)


@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('Name')
    return name

if __name__ == '__main__':
    app.run(debug=True)