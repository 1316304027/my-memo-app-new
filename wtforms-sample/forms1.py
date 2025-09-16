from wtforms import Form, EmailField
from wtforms.fields import (
    StringField, IntegerField,PasswordField,DateField,
    RadioField, SelectField, BooleanField,TextAreaField,
    EmailField,SubmitField
)
#=========================================================
#Formクラス
#=========================================================
# ユーザー情報クラス
class UserInForm(Form):
    # 名前：文字列入力
    name = StringField("名前:",render_kw={"placeholder":
    "小瘪三"})
    # 年齢：整数値入力
    age = IntegerField("年齢：",default=22)
    #パスワード：パスワード入力
    password=PasswordField('パスワード：')
    # 確認用：パスワード入力
    confirm_password = PasswordField('パスワード確認：')
    # Email:メールアドレス入力　邮箱输入框，必须填写且格式要正确
    email = EmailField("メールアドレス：")
    # 生年月日：日付入力
    birthday = DateField('生年月日:',format="%Y-%m-%d",render_kw={"placeholder":
    "yyyy/mm/dd"})
    # 性别：ラジオボタンM代表男，F代表女
    gender = RadioField(
        '性別：', choices=[('man', '男性'), ('woman', '女性')],default='man')
    # 地址多行文本框
    #Address = TextAreaField("Address")
    # 出身地域：セレクトボックス
    area = SelectField('出身地域：', choices=[('east', '東日本'), ('west', '西日本')])
    #既婚：真偽値入力
    is_married=BooleanField('既婚?：')
    # メッセージ：複数行テキスト
    note=TextAreaField('備考：')
    # 提交按钮
    submit = SubmitField("送信")
