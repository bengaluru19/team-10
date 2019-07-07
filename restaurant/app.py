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

@app.route('/admin_dashboard.html')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/client_dashboard.html')
def client_dashboard():
    return render_template('client_dashboard.html')

@app.route('/client.html')
def client_page():
    return render_template('client.html')

@app.route('/survey_form.html')
def survey1():
    return render_template('survey_form.html')

@app.route('/clientLogin.html')
def clientLogin():
    return render_template('clientLogin.html')

@app.route('/adminLogin.html')
def adminLogin():
    return render_template('adminLogin.html')

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
    receiver = receiver[0][0]
    print(receiver)


    # body = "Hello Dude"

    yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

    contents = ['C:/Users/gowda/Desktop/restaurant/templates/welcome.html']
    yag.send(
        to = receiver,
        subject="Hello from AntHills",
        contents = contents
    )

    print('*******')
    return 'success'


@app.route('/survey', methods = ['POST'])
def survey():

    print("ssuurrvey")
    location = request.form['location']
    snake = request.form['snake']
    email = request.form['email']
    area = request.form['area']
    minage = request.form['minage']
    maxage = request.form['maxage']
    budget = request.form['budget']
    disability = request.form['disability']
    maintenance = request.form['maintenance']

    # print(location,snake,disability,maintenance)
    # print(email)
   
    cursor.execute("insert into project (location,email, siteArea, minAge, maxAge, budget, speciallyAbledChildren, requireMaintainance,snakeprone) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (location,email, area, minage, maxage,budget,disability,maintenance,snake))
    con.commit()

    if(snake=='true'):
        receiver = email
    
        # body = path
        contents = ['C:/Users/gowda/Desktop/restaurant/templates/ty.html']
        yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

        yag.send(
            to=receiver,
            subject="Hello from AntHills",
            contents = contents,
            attachments = 'SnakeProne1.pptx'
        )

    if(disability=='true'):
        
        receiver = email
    
        # body = path
        contents = ['C:/Users/gowda/Desktop/restaurant/templates/ty.html']
        yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

        yag.send(
            to=receiver,
            subject="Hello from AntHills",
            contents = contents,
            attachments = 'Disability.pptx'
        )

    else:
        receiver = email
    
        # body = path
        contents = ['C:/Users/gowda/Desktop/restaurant/templates/ty.html']
        yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

        yag.send(
            to=receiver,
            subject="Hello from AntHills",
            contents = contents,
            attachments = 'Standard1.pptx'
        )

    
    # receiver = email
 
    # # body = path

    # yag = yagmail.SMTP("codeforgoodteam101@gmail.com", password = "")

    # yag.send(
    #     to=receiver,
    #     subject="Test",
    #     contents = body,
    #     attachments = path
    # )
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)