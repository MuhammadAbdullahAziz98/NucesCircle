from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def send(request):
    return render(request,'sendmail/send.html')

def email(request):
    recipient = request.POST.get('to','')
    recipient_list=[]
    recipient_list.append(recipient)
    subject = request.POST.get('subject','')
    message = request.POST.get('messages','')
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, recipient_list )
    messages.success(request,"Email sent successfully")

    return redirect('sendmail:send')