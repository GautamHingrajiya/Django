from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    if "email" in request.session:
        return render(request,"myapp/index.html")
    else:
        return render(request,"myapp/login.html")

def login(request):
    
    if request.POST:

        p_email = request.POST['email']
        p_password = request.POST['password']

        try:
            uid = User.objects.get(email = p_email)
            if uid.password == p_password:
                if uid.role == "Chairman":
                    cid = Chairman.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    return render(request,"myapp/index.html")
                else:
                    pass
            else:
                context = {
                    'e_msg':'Invalid Password'
                }
                return render(request,"myapp/login.html",context)
        except:
                context = {
                    'e_msg':'Invalid Email'
                }
                return render(request,"myapp/login.html",context)
            
    else:

        print("<<<<<<<<<<================= Only Referes ================== ")
    
    return render(request,"myapp/login.html")
