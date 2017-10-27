from flask import url_for, Flask, redirect

app = Flask(__name__)


@app.route('/static/新闻标题')
def index():
    return redirect(url_for('static', filename='新闻标题.html'))


if __name__ == '__main__':
    app.run(debug=True)

