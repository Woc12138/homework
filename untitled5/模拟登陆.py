from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from wtforms import StringField, SubmitField

app = Flask(__name__)

bootstrap =Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
class NameForm1(Form):
    id = StringField('student_id:', validators=[Required()])


class NameForm2(Form):
    password = StringField('password', validators=[Required()])
    submit = SubmitField('Submit')
def login():
    username = input("请输入用户名：")
    user_password = inquire_userlist(username) #查询输入用户名是否存在注册用户名单中，若存在则返回该用户密码
    if user_password:
        for i in range(3):
            password = input("请输入密码：") if i==0 else input("密码输入错误，请重新输入密码：")
            if password == user_password:
                print('欢迎%s登陆!'%username)
                return True
