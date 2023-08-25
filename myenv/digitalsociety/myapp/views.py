from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,"myapp/index.html")

def login(request):
    
    if request.POST:
        p_email = request.POST['email']
        p_password = request.POST['password']

        uid = User.objects.get(email = p_email)
        print("\n\t\n\t UID Object :",uid )

        if uid.role=="Chairman":
            cid = Chairman.objects.get(user_id = uid)
            print(cid)
        else:
            pass
        
        

        # if uid.password == p_password:
        #     print("valid Password")
         
        # else:
        #     print("Invalid Password")

    else :
        print("\n\n\t\tonly refresh")

    return render(request,"myapp/login.html")