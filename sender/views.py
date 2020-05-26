from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method == "GET":
        return render(request, 'sender/home.html')
    else:
        sender = request.POST.get('sender')
        mail_service = sender.find('@')
        mail_service = sender[mail_service+1:]
        if mail_service == 'gmail.com':
            settings.EMAIL_PORT = 587
        settings.EMAIL_HOST += mail_service
        settings.EMAIL_HOST_USER = sender
        password = request.POST.get('password')
        settings.EMAIL_HOST_PASSWORD = password
        recipient = request.POST.get('recipient')
        recipient = recipient.split(',')
        topic = request.POST.get('topic')
        message = request.POST.get('message')

        send_mail(subject=topic, message=message, from_email=settings.EMAIL_HOST_USER, recipient_list=recipient, fail_silently=False)

        return render(request, 'sender/home.html', {'result': 'Message sent!'})
