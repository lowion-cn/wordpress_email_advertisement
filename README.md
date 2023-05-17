# wordpress_email_advertisement
当文章更新时自动向所有注册在Wordpress博客上的用户发送提醒邮件<br />
具体介绍可看：https://www.lowion.cn/2023/02/992/<br />
主程序就是index.py<br />
需要用到以下库：<br />
import time<br />
import pymysql<br />
import smtplib<br />
from email.mime.text import MIMEText<br />
from email.header import Header<br />
import feedparser<br />
可以使用以下命令安装：<br />
pip install time pymysql smtplib email feedparser<br />
然后根据index.py代码中的提示填入服务器和Wordpress信息即可
