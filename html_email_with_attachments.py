import mimetypes
import smtplib
import ssl
from email.message import EmailMessage


SERVER_ADDRESS = "YOUR_SERVER_ADDRESS"  # smtp.live.com for example
SERVER_PORT = 587
EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS@EXAMPLE_DOMAIN.COM'
EMAIL_PASSWORD = 'YOUR_PASSWORD'
RECIPIENT_EMAIL = 'RECIPIENT_EMAIL@EXAMPLE_DOMAIN.COM'

# Email content
msg = EmailMessage()

msg['Subject'] = "My Custom Subject"
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPIENT_EMAIL

msg.set_content('Hello World')

msg.add_alternative("""
<p>
    <h1>My Custom Title</h1>
    Hello <strong>World</strong>
</p>
""", subtype='html')


filename = 'attachment.txt'
path = f'docs/{filename}'

# Guess the content type based on the file's extension.
ctype, encoding = mimetypes.guess_type(path)
if ctype is None or encoding is not None:
    ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)

with open(path, 'rb') as fp:
    msg.add_attachment(fp.read(), maintype=maintype, subtype=subtype,
                       filename=filename)


# Create a SSLContext object with default settings.
context = ssl.create_default_context()

with smtplib.SMTP(SERVER_ADDRESS, SERVER_PORT) as smtp:
    smtp.ehlo()  # Say EHLO to server
    smtp.starttls(context=context)  # Puts the connection in TLS mode.
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)  # Auto detects the sender and recipient from header
