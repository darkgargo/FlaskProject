from flask import Flask,render_template
from flask.globals import request
import pymysql


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('SignUp.html')
  #메인화면 route


#회원 가입 진행시 Route
@app.route('/Sign-Up', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        value = request.form['id_name']
        value = str(value)
        value2=request.form['pw_name']
        value2=str(value2)
        value3=request.form['name_name']
        value3=str(value3)
        insert_table(value,value2,value3)
        Result=show_table()
    return render_template('SignIn.html',id_list=Result)

# #로그인 진행 루트
# @app.route('Sign-In', methods=['GET','POST'])
# def post():
#     if request.method=='POST':
#         id_check=request.form['id_name']
#         pw_check=request.form['pw_name']
#         id_list=[]
#         pw_list=[]
#         id_list.append(show_Id_table())
#         pw_list.append(show_Pw_table())

#     return id_list


#테이블 전체 조회 함수
def show_table():
    db = pymysql.connect(host='20.194.51.62', port=3306, user='connector', passwd='password12!@', db='SignIn', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT * FROM aksmember;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)

#테이블 ID 조회 함수
def show_Id_table():
    db = pymysql.connect(host='20.194.51.62', port=3306, user='connector', passwd='password12!@', db='SignIn', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT id FROM aksmember;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)
    
#테이블 password 조회 함수
def show_Pw_table():
    db = pymysql.connect(host='20.194.51.62', port=3306, user='connector', passwd='password12!@', db='SignIn', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT password FROM aksmember;'''
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return str(result)


#TABLE INSERT 함수
def insert_table(ID,PW,NAME):
    db = pymysql.connect(host='20.194.51.62', port=3306, user='connector', passwd='password12!@', db='SignIn', charset='utf8')
    cursor = db.cursor()
    sql="INSERT INTO aksmember VALUES('%s','%s','%s')" %(ID,PW,NAME)
    cursor.execute(sql)
    result=cursor.fetchall()
    db.commit()
    db.close()
    a=show_table() #Insert 후 조회하기
    print(a)
    return a;


if __name__ == '__main__':
    app.run()
