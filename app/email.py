from threading import Thread
from . import mail
from flask_mail import Message
from flask import current_app, render_template


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

    if app.config['DEBUG'] == True and not app.config['TESTING'] :
        log_email_to_console(app, msg) # logs email to console
    return thr


def log_email_to_console(app, msg):
    """
    Prints email body to console in dev environment
    """
    app.logger.info(msg.body)
    app.logger.info ('|=== email ends ===|')
