import pymysql
import sys
sys.path.append('d:/Sourcetree_account')
import pymysql_con
from werkzeug.security import generate_password_hash

pwd = generate_password_hash('cat')
username = 'abc'
email = 'sdkjweiu@gmail.com'
conn = pymysql.connect(host='192.168.182.128', port=3306, user=pymysql_con.user, passwd=pymysql_con.passwd, database='flasky')
cur = conn.cursor()
cur.execute('insert into user(username, password_hash, email) values("%s", "%s", "%s") '%(username, pwd, email))
conn.commit()
cur.close()
conn.close()