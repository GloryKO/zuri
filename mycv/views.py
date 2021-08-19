from django import forms
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from mytask import settings
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data["name"]
            email =form.cleaned_data["email"]
            message =form.cleaned_data["message"]
            send_mail(f" {name} sent an email",message,email,[settings.EMAIL_HOST_USER],fail_silently=False)
            messages.success(request,f"Message sent sucessfully")
    else:
        form = ContactForm()
    context = {"form":form}
    return render(request,'mycv/mycv.html',context)