import sendgrid
from sendgrid.helpers.mail import *
SENDGRID_APIKEY = 'This is your SendGrid API key'

def _send_mail(subj, body, to_e):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_APIKEY)
    # This from address is require verify from SendGrid
    from_email = Email("your from email address")
    to_email = To(to_e)
    subject = subj
    content = Content("text/html", body)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.send(mail)
    return response
if __name__ == "__main__":
    print('This function can be imported and called within another Python script')
    print('Email from is hardcode as SendGrid require this address to be verified')
    print('Passing parameters: subject line, message body, and mail to address')
    print('-------------------------------------------------------')
    print('_send_mail(Message Subject, Message body, To address)')
