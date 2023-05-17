# 作者(Author)：WilliamSun
# 链接(URL)：https://www.lowion.cn/2023/02/992/

import time
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import feedparser
 
def sendmain(url):
    db = pymysql.connect(host='你服务器的ip', user="数据库用户名", passwd="数据库密码", db='数据库名称', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = """SELECT * FROM wp_users"""
    cursor.execute(sql)
    desc = cursor.description
    data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
    cursor.close()
    db.close()
 
    print(data_dict)
    for i in range(len(data_dict)):
        sendsmtpm(url,data_dict[i]['user_email'])
        print('成功发送给：'+data_dict[i]['user_email'])
def sendsmtpm(url,to):
    smtp = smtplib.SMTP()
    smtp.connect("你的smtp服务器", port=25)
    smtp.login(user="你的smtp用户名", password="smtp服务器用户名对应的密码")
    message = MIMEText('xxxxx新文章更新了：'+url)# 发送的一段文字，url变量是更新的文章地址
    message['From'] = Header("xxxxx",'utf-8')  # 发件人的昵称
    message['Subject'] = 'xxxxx有文章更新啦'  # 定义主题内容
    print(message)
 
    smtp.sendmail(from_addr="smtp发送者邮箱，一般跟用户名相同", to_addrs=to, msg=str(message))
    smtp.close()
rss_oschina = feedparser.parse('你的RSS链接')
first=[rss_oschina['entries'][0]['links'][0]['href'],rss_oschina['entries'][1]['links'][0]['href'],rss_oschina['entries'][2]['links'][0]['href'],rss_oschina['entries'][3]['links'][0]['href'],rss_oschina['entries'][4]['links'][0]['href'],rss_oschina['entries'][5]['links'][0]['href']]
print('Start')
print(first)
while True:
    rss_oschina = feedparser.parse('你的RSS链接')
    send=True
    for i in range(len(first)):
        if first[i]==rss_oschina['entries'][0]['links'][0]['href']:
            send=False
    if send:
        sendmain(rss_oschina['entries'][0]['links'][0]['href'])
        print('stmpsend：'+rss_oschina['entries'][0]['links'][0]['href'])
        first.append(rss_oschina['entries'][0]['links'][0]['href'])
    time.sleep(5)

import time
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import feedparser
 
def sendmain(url):
    db = pymysql.connect(host='你服务器的ip', user="数据库用户名", passwd="数据库密码", db='数据库名称', port=3306, charset='utf8')
    cursor = db.cursor()
    sql = """SELECT * FROM wp_users"""
    cursor.execute(sql)
    desc = cursor.description
    data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
    cursor.close()
    db.close()
 
    print(data_dict)
    for i in range(len(data_dict)):
        sendsmtpm(url,data_dict[i]['user_email'])
        print('成功发送给：'+data_dict[i]['user_email'])
def sendsmtpm(url,to):
    smtp = smtplib.SMTP()
    smtp.connect("你的smtp服务器", port=25)
    smtp.login(user="你的smtp用户名", password="smtp服务器用户名对应的密码")
    message = MIMEText('xxxxx新文章更新了：'+url)# 发送的一段文字，url变量是更新的文章地址
    message['From'] = Header("xxxxx",'utf-8')  # 发件人的昵称
    message['Subject'] = 'xxxxx有文章更新啦'  # 定义主题内容
    print(message)
 
    smtp.sendmail(from_addr="smtp发送者邮箱，一般跟用户名相同", to_addrs=to, msg=str(message))
    smtp.close()
rss_oschina = feedparser.parse('你的RSS链接')
first=[rss_oschina['entries'][0]['links'][0]['href'],rss_oschina['entries'][1]['links'][0]['href'],rss_oschina['entries'][2]['links'][0]['href'],rss_oschina['entries'][3]['links'][0]['href'],rss_oschina['entries'][4]['links'][0]['href'],rss_oschina['entries'][5]['links'][0]['href']]
print('Start')
print(first)
while True:
    rss_oschina = feedparser.parse('你的RSS链接')
    send=True
    for i in range(len(first)):
        if first[i]==rss_oschina['entries'][0]['links'][0]['href']:
            send=False
    if send:
        sendmain(rss_oschina['entries'][0]['links'][0]['href'])
        print('stmpsend：'+rss_oschina['entries'][0]['links'][0]['href'])
        first.append(rss_oschina['entries'][0]['links'][0]['href'])
    time.sleep(5)
