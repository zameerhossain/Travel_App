from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Destination,Contact,Contact_Blog




# Create your views here.
def contact(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact_blog=Contact_Blog(name=name,email=email,subject=subject,message=message)
        contact_blog.save()
        messages.info(request, 'Message recived')
        return redirect('contact')

    else:
        con_info=Contact.objects.all()
        return render(request,"contact.html",{'con_info':con_info})

def index(request):
    dests=Destination.objects.all()

    offer_count=Destination.objects.filter(offer=True).count()
    return render(request,"index.html",{'dests':dests,'offer_count':offer_count})


