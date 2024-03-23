from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message[ "from" ] = "Jesus"
# message[ "to" ] = "jesus@phss.com"
# message[ "to" ] = "photocromatic@gmail.com"
message[ "to" ] = "iot.ech.fun@gmail.com"
message[ "subject" ] = "This is a Jesús Message"
message.attach( MIMEText( "Body " ) )

with smtplib.SMTP( host = "smtp.gmail.com", port = 587 ) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login( "jesus@phss.com", "JHS337" )
    smtp.login( "photocromatic@gmail.com", "PASSWORD" )
    smtp.send_message( message )

    print( "Mail has been sent..!" )
