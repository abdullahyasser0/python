from email.message import EmailMessage
import smtplib
import ssl



email_sender='from@gmail.com'
email_password='16 char generated password' #turn on 2step verification then go to https://myaccount.google.com/u/4/apppasswords
email_reciver='to@gmail.com'



subject='subject'
body="""text"""



em = EmailMessage()
em['From']=email_sender
em['to']=email_reciver
em['subject']=subject
em.set_content(body)



context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender,email_reciver,em.as_string())
