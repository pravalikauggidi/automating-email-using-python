import smtplib
from email.mime.multipart import MIMEMultipart
MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
   # Email configurations
   smtp_server="smtp.puggidi@gmail.com"
   smtp_port = 587
   sender_email = "puggidi@gmail.com"
   sender_password = "ials laqj yvle puts"
   recipient_email = "pravalikauggidi@gmail.com"
   subject = "Automated Email"
   body = "hello"

  # Create the email message
   message = MIMEMultipart()
   message['From'] = sender_email
   message['To'] = recipient_email
   message['Subject'] = subject

  # Attach the email body to the message
   body="this is an automated email sent using python"
   message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", "587")
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login("puggidi@gmail.com", "ials laqj yvle puts")  # Login to the email account    text = "message".as_string()  # Convert the message to a string
    server.sendmail("puggidi@gmail.com", "pravalikauggidi@gmail.com", "hello")  # Send the email
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')

schedule.every().day.at("09:00").do(send_email)    #1:00  pm

while True:
 schedule.run_pending()
 time.sleep(1)
