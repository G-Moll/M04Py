from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


message = MIMEMultipart()
message[ 'from' ] = 'JHS'
# message[ 'to' ] = 'iot.ech.fun@gmail.com'
message[ 'to' ] = 'alejita29.af@gmail.com'
message[ 'subject' ] = 'This is a message from ' + message[ 'from' ]
message_body = """
Hello Ale..! 😄
I am """ + message[ 'from' ] + """
nice to meet you..! 👋
"""

message.attach( MIMEText( message_body ) )

with smtplib.SMTP( host = 'smtp.gmail.com', port = 587 ) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login( 'photocromatic@gmail.com', 'password' )
    smtp.send_message( message )

    print( 'Mail has been sent..!' )

# https://emojipedia.org/smileys

