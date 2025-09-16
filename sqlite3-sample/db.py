import os
import sqlite3

#===========================================
# DBファイル生成
#===========================================

base_dir = os.path.dirname(__file__)
# os.path.dirname(__file__)：获取当前脚本文件所在的目录路径
# base_dir：存储数据库文件存放位置的变量
database = os.path.join(base_dir,'data.sqlite')
# os.path.join()：拼接路径和文件名
# 'data.sqlite'：数据库文件名
# database：数据库文件的完整路径（如：C:/project/data.sqlite）
#===========================================
#SQL
#===========================================
#接続
conn = sqlite3.connect(database)
# sqlite3.connect()：建立数据库连接
# conn：数据库连接对象，后续所有数据库操作都通过它进行
print('▼▼▼▼▼▼▼▼▼▼ コネクションの接続 ▼▼▼▼▼▼▼▼▼▼')
print()
# カーソル
# 创建游标对象
cur = conn.cursor()
# cursor()：创建游标对象
# cur：游标实例，用于执行SQL语句和获取结果
# テーブル削除SQL
drop_sql = """
    DROP TABLE IF EXISTS items;
"""
# DROP TABLE：SQL删除表命令
# IF EXISTS：安全删除（仅当表存在时才删除）
# items：要删除的表名
cur.execute(drop_sql)
# execute()：执行SQL语句
print('(1)対象テーブルがあれば削除')
#テーブル作成SQL
# 创建新表
create_sql = """
    CREATE TABLE items(
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name STRING UNIQUE NOT NULL,
        price INTEGER NOT NULL) 
    """
# CREATE TABLE：创建表命令
# item_id：商品ID列（主键，自动增长）
# item_name：商品名列（唯一且不能为空）
# price：价格列（整数类型，不能为空）
cur.execute(create_sql)
print('(2)テーブル作成')
#データ登録SQl
insert_sql="""
    INSERT INTO items (item_name,price) VALUES (?,?)
    """
# INSERT INTO：插入数据命令
# (item_name,price)：指定要插入的列
# VALUES (?,?)：参数占位符（防止SQL注入攻击）
insert_data_list= [
    ('団子',100),('肉まん',150),('どら焼き',200)
]
# 要插入的数据列表，每个元组对应一行数据
cur.executemany(insert_sql,insert_data_list)
# executemany()：批量执行SQL语句（比循环执行execute()更高效）
conn.commit()
# commit()：提交事务（使数据修改永久生效）
print('(3)データ登録：実行')
#データ参照(全件)SQL
# 查询所有数据
select_all_sql = """
    SELECT * FROM items
    """
# SELECT * ：查询所有列
# FROM items：从items表中查询
cur.execute(select_all_sql)
print('(4)----------　全件取得：実行　----------')
data = cur.fetchall()
# fetchall()：获取所有查询结果（返回列表格式）
print(data)
#データ参照(1件)SQL
select_one_sql = """
    SELECT*FROM items WHERE item_id = ?
    """
# WHERE item_id = ?：按商品ID查询（?是参数占位符）
id =3
cur.execute(select_one_sql,(id,))
# (id,)：单元素元组（必须有逗号，否则不是元组）
print('(5)----------　1件取得：実行　----------')
data = cur.fetchone()
# fetchone()：获取单条查询结果（返回元组格式）
print(data)
#データ更新SQL
update_sql="""
    UPDATE items SET price=? WHERE item_id=?
    """
# UPDATE：更新命令
# SET price=?：设置新价格
# WHERE item_id=?：指定要更新的记录
price=500
id=1
cur.execute(update_sql,(price,id))
print('(6)----------　データ更新：実行　----------')
conn.commit()
cur.execute(select_one_sql,(id,))
data = cur.fetchone()
print('確認のため１件取得：実行',data)
#データ削除SQL
delete_sql="""
    DELETE FROM items WHERE item_id =?
    """
id=3
cur.execute(delete_sql,(id,))
conn.commit()
print('(7)----------　データ削除：実行　----------')
cur.execute(select_all_sql)
data = cur.fetchall()
print('確認のため全件取得:実行',data)
#閉じる
# 关闭数据库连接
conn.close()
print()
print('▲▲▲▲▲▲▲▲▲▲ コネクションを閉じる ▲▲▲▲▲▲▲▲▲▲')



