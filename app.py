from flask import Flask, render_template, request,Response
import pymysql
import repository as rp
import logging as log

app = Flask(__name__)

###### View 관련 기본적인 라우팅 ######
## View 기본적인 활용
@app.route('/view/render/basic')
def view_render_basic():  # put application's code here
    return render_template('html/index.html')

## View 데이터 전달
@app.route('/view/render/data')
def view_render_basic():  # put application's code here
    # 기본 데이터
    msg = 'test'
    # 리스트
    list = ['list1','list2','list3','list4']
    # 딕셔너리(JSON)
    dic = dict()
    dic['dic1'] = 'dic_msg1'
    dic['dic2'] = 'dic_msg2'
    dic['multi_dic'] = dict()
    dic['multi_dic']['dic1'] = 'multi_dic1_msg'
    
    return render_template('html/index.html', msg=msg,list=list,dic=dic)

if __name__ == '__main__':
    app.run()



###### 로그 관련하여 ######
log = log.getLogger()



###### DB(데이터베이스) 관련하여 #########

# DB init
conn_prod = pymysql.connect(host='172.30.1.66', user='jelly', password='Jellynice1!', port=3307, db='prod')
cur_prod = conn_prod.cursor()