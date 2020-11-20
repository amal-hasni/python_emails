import pandas as pd
from Dmail.esp import Hotmail

# Email template creation
template = """
Dear {reader},

This is just an email example containing:

- The **banner image** as an inline image

- The **SMTP addresses table**, with *centered cell values*, some *background colors* and *automatically adjusted height*

- A csv **file attached**

Here's the table:

{smtp_table}

You can also find below the article banner:

![Article Banner Image]({image_path})

Best regards,

{sender}
"""

# Import the table from the csv file in a pandas dataframe
table_path = "my_table_csv_file"
smtp_table = pd.read_csv(table_path, sep=";", index_col=None)

# Get image path
image_path = "my_banner_image_path"


# Function that highlights odd rows with specific color in a pandas dataframe
def highlight_odd_rows(s):
    return ['background-color: #CEF8BE' if s.name % 2 else '' for v in s]


# Styling the dataframe using pandas' .style
smtp_table = (smtp_table.style
              # .set_caption("SMTP addresses table")      # Add caption to table
              .set_properties(**{'text-align': 'center',  # Align cell values to center
                                 'margin': 'auto'})  # Adjust cell sizes automatically
              .set_table_styles([{'selector': 'th',
                                  'props': [('background-color', '#6BE63E'),  # Add background color to header
                                            ('margin', 'auto')]}])  # Adjust header cell sizes automatically
              .apply(highlight_odd_rows, axis=1)  # Add background color to odd rows
              .hide_index()  # Export the table without the index column
              .render())

# Adding personal information
user = "Jane Doe"
sender_name = "John Doe"
email_address = "my_email_adress"
password = "my_email_password"
recipient_email = "recipient_email_adress"

# Creating the email body
message = template.format(reader=user, sender=sender_name, image_path=image_path, smtp_table=smtp_table)

# Sending the email
with Hotmail(email_address, password) as email:
    email.send(message, recipient_email, attachments=[table_path],
               subject=f"Demonstration of mail sending using Dmail library")
