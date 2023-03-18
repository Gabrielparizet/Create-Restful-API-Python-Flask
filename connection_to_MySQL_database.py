from flask import Flask
from flaskext.mysql import MySQL
from getpass4 import getpass

user = getpass('User:')
password = getpass('Password:')
database = getpass('Database:')
host = getpass('Host:')

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = database
app.config['MYSQL_DATABASE_HOST'] = host
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

cursor.execute("SELECT * from furniture")
data = cursor.fetchone()
print(data)

