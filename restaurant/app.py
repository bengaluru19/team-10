from flask import Flask, request, render_template, Response
from flaskext import mysql
import yagmail
import mysql.connector

# global reciever

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

@app.route('/survey_form.html')
def survey1():
    return render_template('survey_form.html')

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
    globals() ['receiver'] = receiver[0][0]
    print(receiver)


    body = "Hello Dude"

    yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

    yag.send(
        to=receiver,
        subject="Test",
        contents = body
    )

    print('*******')
    return 'success'


@app.route('/survey', methods = ['POST'])
def survey():

    print("ssuurrvey")
    location = request.form['location']
    snake = request.form['snake']
    email = request.form['email']
    
    disability = request.form['disability']
    maintenance = request.form['maintenance']

    print(location,snake,disability,maintenance)
    print(email)
    # cursor.execute("insert into project (location,snakeprone,email) values (%s,%s,%s)", (location,phone,email))
    # con.commit()

    # cursor.execute("select email from client order by cid desc limit 1")
    
    # receiver = cursor.fetchall()
    # receiver = receiver[0][0]
    # print(receiver)
    # body = "Hello Dude"

    # yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

    # yag.send(
    #     to=receiver,
    #     subject="Test",
    #     contents = body
    # )

    # print('*******')
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)