import os
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#======================================================================================
# インスタンス生成
#======================================================================================
app = Flask(__name__)

#======================================================================================
# Flaskに対する設定
#======================================================================================
import  os
# 乱数を設定
app.config['SECRET_KEY']=os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir,'newdata.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']=database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# ★db変数を使用してSQLALchemyを操作できる
db=SQLAlchemy(app)
# ★「flask_migrate」を使用できる様にする
Migrate(app,db)

#======================================================================================
# モデル
#======================================================================================
#課題
class Task(db.Model):
    #　テーブル名
    __tablename__ = 'tasks'

    #課題ID
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    #内容
    content = db.Column(db.String(200), nullable=False)
    # 完了フラグ
    is_completed =db.Column(db.Boolean,default=False)

    #表示用
    def __str__(self):
        return f'課題ID:{self.id}　内容：{self.content}'

#======================================================================================
# モデル
#======================================================================================
#一览
@app.route('/')
def index():
    # 未完了課題を取得
    uncompleted_tasks = Task.query.filter_by(is_completed=False).all()
    # 完了課題を取得
    completed_tasks = Task.query.filter_by(is_completed=True).all()
    return render_template('index.html',uncompleted_tasks=uncompleted_tasks,
                           completed_tasks=completed_tasks)

#登録
@app.route('/new',methods=['GET','POST'])
def new_task():
    #POST
    if request.method == 'POST':
        # 入力値取得
        content = request.form['content']
        #インストール生成
        task = Task(content=content)
        #登録
        db.session.add(task)
        db.session.commit()
        #一覧へ
        return redirect(url_for('index'))
    #GET
    return render_template('new_task.html')

# 完了
@app.route('/tasks/<int:task_id>/complete',methods=['POST'])
def complete_task(task_id):
    # 对象データ取得
    task = Task.query.get(task_id)
    # 完了フラグに「True」を設定
    task.is_completed=True
    db.session.commit()
    return redirect(url_for('index'))

# 未完了
@app.route('/tasks/<int:task_id>/uncomplete',methods=['POST'])
def uncomplete_task(task_id):
    #対象データ取得
    task = Task.query.get(task_id)
    #完了フラグに「False」を設定
    task.is_completed = False
    db.session.commit()
    return redirect(url_for('index'))

#======================================================================================
# 実行
#======================================================================================
if __name__ == '__main__':
    app.run()

"""#▼▼▼▼▼ リスト7.3追加 ▼▼▼▼▼
#======================================================================================
# CRUD操作
#======================================================================================
#登録

def insert():
    with app.app_context():
        print('================ 3件登録 ================')
        #データ作成
        print('(1)データ登録：実行')
        task01 = Task(content='風呂掃除')
        task02 = Task(content='洗濯ahsdhdsjsdsa')
        task03 = Task(content='買い物')
        db.session.add_all([task01, task02, task03])
        db.session.commit()

#======================================================================================
# 実行
#======================================================================================
if __name__ == '__main__':
    insert()    #データ登録
#▲▲▲▲▲ リスト7.3追加 ▲▲▲▲▲

"""