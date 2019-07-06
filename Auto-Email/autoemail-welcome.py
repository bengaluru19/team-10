# import yagmail module.
import yagmail
# connect to smtp server.
yag_smtp_connection = yagmail.SMTP( user="codeforgoodteam101@gmail.com", password="", host='smtp.gmail.com')# email subject
subject = 'Hello from richard'
# email content with attached file path.
contents = ['/home/kaushiksingh/team-10/Auto-Email/welcome.html']
# send the email
yag_smtp_connection.send('kaushiksingh001@gmail.com', subject, contents)
