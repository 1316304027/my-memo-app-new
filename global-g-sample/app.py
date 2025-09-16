from flask import Flask, g, request

#======================================================================================
# インスタンス生成
#======================================================================================
app = Flask(__name__)

#======================================================================================
# ルーティング
#======================================================================================
@app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def do_hello():
    user = g.user
    return f'hello {user}'

@app.route('/morning')
def do_morning():
    user=g.user
    return f'morning {user}'

@app.route('/evening')
def do_evening():
    user=g.user
    return f'evening {user}'

#
def get_user():
    user_info={
        "name":"大G",
        "age": 23,
        "email":"g.da@example.com"
    }
    return user_info

#======================================================================================
# 実行
#======================================================================================
if __name__ == '__main__':
    app.run()