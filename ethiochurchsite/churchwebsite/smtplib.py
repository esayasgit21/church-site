import smtplib
from email.message import EmailMessage
from django import forms

"""server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.sendmail('gizaw.esayas@yahoo.com','gizaw.esayas@gmail.com','Mil from python')
print('Mail sent') 

email_sender = 'gizaw.esayas@yahoo.com'
email_receiver = 'gizaw.esayas@gmail.com'
subject = 'This is Python Test Email'
message = 'i have just published a new webapp'
email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_receiver,'#16846Gmail21')
    smtp.sendmail(email_sender,email_receiver,email.as_string())
    """

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 50)   
    name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 150)
    message = forms.CharField(max_length = 2000)


