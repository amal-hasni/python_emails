import smtplib
import ssl

SERVER_ADDRESS = "YOUR_SERVER_ADDRESS"  # smtp.live.com for example
SERVER_PORT = 587
EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS@EXAMPLE_DOMAIN.COM'
EMAIL_PASSWORD = 'YOUR_PASSWORD'
RECIPIENT_EMAIL = 'RECIPIENT_EMAIL@EXAMPLE_DOMAIN.COM'

# Email content
email_subject = "My Custom Subject"
email_sender = EMAIL_ADDRESS
email_recipient = RECIPIENT_EMAIL

message = f"""\
Subject: {email_subject}
From: {email_sender}
TO: {email_recipient}

Hello World"""


# Create a SSLContext object with default settings.
context = ssl.create_default_context()

with smtplib.SMTP(SERVER_ADDRESS, SERVER_PORT) as smtp:
    smtp.ehlo()  # Say EHLO to server
    smtp.starttls(context=context)  # Puts the connection in TLS mode.
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, message)

