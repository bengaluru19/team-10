import yagmail

# yagmail.register('gmailusername','password')    #do this once

receiver = "alwaysharsh47@gmail.com"
body = "Hello there from Yagmail"                #can be an html script
# filename = "document.pdf"

yag = yagmail.SMTP("codeforgoodteam101@gmail.com",password="")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body, 
    # attachments=filename,
)