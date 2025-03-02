from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from student_management_app import EmailBackEnd

# Create your views here.
def showDemoPage(request):
    return render(request, "demo.html")


def showLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            return HttpResponse("Email: " + request.POST.get("email") + " Password: " + request.POST.get("password"))
        else:
            return HttpResponse("Invalid Login fix this")

    

def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User : " + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

