import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '44f5192c9da38d'
    password = '49c8c0ce4a9cd1'
    message = f'<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'
    
    sender_email = 'email1@gmail.com'
    reciever_email = 'email2@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Square Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email
    
    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())