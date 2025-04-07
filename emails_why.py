from email.message import EmailMessage
import ssl
import smtplib
# Set up the server and your email details
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "oyeneyinfemisayo@gmail.com"
receiver_email = "femiayo2.0@gmail.com"
password = 'vcrt miah mhba qkro'

subject='hey'
body= "hello hello how are you"
em = EmailMessage()
em['From']= sender_email
em['To']= receiver_email
em ['Subject']= subject
em.set_content(body) 

contexts=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,smtp_port, context=contexts) as smtp:
    smtp.login(sender_email,password)
    smtp.send_message(em)