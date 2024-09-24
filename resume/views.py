from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from datetime import datetime
from resume.models import Contact
from django.contrib import messages

# Create your views here.

def home (request):
    return render(request,"home.html")

def about (request):
    return render(request,"about.html")


def projects (request) :
    projects_show=[
        {
            "tittle":"Wadapav Application",
         "path":"images/wadapav.jpg"
        },

        {
            "tittle":"Portfolio",
         "path":"images/portfolio.jpg"
        },

        {
            "tittle":"Spotify Clone",
         "path":"images/spotify.jpg"
        }
    ]
    return render(request,"projects.html",{"projects_show":projects_show})

def certificate (request) :
    certificates_show=[
        {"tittle":"Python Programming",
         "path":"images/Python.png"
        },

        {"tittle":"CSS Programming",
         "path":"images/css.png"
        },
    ]
    return render(request,"certificate.html",{"certificates_show":certificates_show})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent !")
    return render(request,"contact.html")

def resume (request):
   resume_path="my resume/Juned_qureshi_django.pdf"
   resume_path=staticfiles_storage.path(resume_path)
   if staticfiles_storage.exists(resume_path):
       with open(resume_path,"rb") as resume_file:
           response=HttpResponse(resume_file.read(),content_type="applcation/pdf")
           response['content-Disposition']='attachment';filename="Juned_qureshi_django.pdf"
           return response
   else:
       return HttpResponse("resume not found", status=404)