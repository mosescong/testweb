from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():

    return '<h>index_page</h>'

@app.route('/signin',methods=['GET'])
def sign_form():
    return '''<form action="/signin" method="post">
            <p><input name="UserName" type="text" /></p>
            <p><input name="PassWord" type="password" /></p>
            <p><button type="submit">signin</button></p>
            </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['UserName']=='admin' and request.form['PassWord']=='password':
        return '<h3>hello admin!</h3>'
    return '<h3>bad username and password!</h3>'


if __name__ == '__main__':
    app.run()