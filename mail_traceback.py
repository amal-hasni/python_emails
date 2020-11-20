import traceback
from Dmail.esp import Hotmail


EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS@EXAMPLE_DOMAIN.COM'
EMAIL_PASSWORD = 'YOUR_PASSWORD'
RECIPIENT_EMAIL = 'RECIPIENT_EMAIL@EXAMPLE_DOMAIN.COM'


try:
    raise Exception('Something went wrong')
except Exception as e:
    # Email Content
    msg = '\n'.join(['# Traceback',
                     '```pytb',
                     traceback.format_exc(),
                     '```'])
    # Sending the email
    with Hotmail(EMAIL_ADDRESS, EMAIL_PASSWORD) as email:
        email.send(msg, RECIPIENT_EMAIL, subject=f'Failed job: {e}')
