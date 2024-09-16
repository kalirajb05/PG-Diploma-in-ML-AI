import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread
from chat_config import EmailConfig

gmail_config = EmailConfig()

def send_async_email(recipient, subject, mail_content):
    #The mail addresses and password
    sender_address = gmail_config[0]
    sender_pass = gmail_config[1]
    receiver_address = recipient
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Rasa Chat BOT - Top 10 Result for Search Restaurant'
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def sendmail(recipient, subject, mail_content):
     thr = Thread(target=send_async_email, args=[recipient, subject, mail_content])
     thr.start()