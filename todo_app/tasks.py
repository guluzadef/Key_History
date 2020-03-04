from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import EmailMultiAlternatives

def addkey(to_mail,key):
    subject, from_email, to = 'Key History', 'quluzadef4@gmail.com', to_mail
    text_content = f'{key}-ADDED'
    html_content = f'{key}-ADDED'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def deletekey(to_mail,key):
    subject, from_email, to = 'Key History', 'quluzadef4@gmail.com', to_mail
    text_content = f'{key}-DELETED'
    html_content = f'{key}-DELETED'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def updatekey(to_mail,key):
    subject, from_email, to = 'Key History', 'quluzadef4@gmail.com', to_mail
    text_content = f'{key}-UPDATED'
    html_content = f'{key}-UPDATED'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@shared_task
def add(x, y):
    return x + y