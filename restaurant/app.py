from flask import Flask, request, render_template, Response
from flaskext import mysql
import yagmail
import mysql.connector

# mysql = mysql()


app = Flask(__name__)
# app.config('MYSQL_DATABASE_USER') = 'root'
# app.config('MYSQL_DATABASE_PASSWORD') = ''
# app.config('MYSQL_DATABASE_DB') = 'anthills'
# app.config('MYSQL_DATABASE_HOST') = 'localhost'
# mysql.init_app(app)
# con = mysql.connect()

con = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'anthills'
)


cursor = con.cursor()

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/client.html')
def client_page():
    return render_template('client.html')

@app.route('/survey.html')
def survey():
    return render_template('survey.html')

@app.route('/register/', methods = ['POST'])
def register():
    print("helllllloooooo")
    email = request.form['email']
    name = request.form['name']
    phone = request.form['phone']

    cursor.execute("insert into client (name,phone,email) values (%s,%s,%s)", (name,phone,email))
    con.commit()

    cursor.execute("select email from client order by cid desc limit 1")
    
    receiver = cursor.fetchall()

    body = "Hello Dude"

    yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

    yag.send(
        to=receiver,
        subject="Test",
        contents = body
    )

    print('*******')

if __name__ == '__main__':
    app.run(debug=True)