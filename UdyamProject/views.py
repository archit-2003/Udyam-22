from django.shortcuts import render ,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def handleSignUp(request):
    if request.method=="POST":
        #Get the POST parameters
        username=request.POST['loginusername']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['loginpassword']
        pass2=request.POST['confirmpassword']

        # check for errorneous input
        if len(username)> 10 :
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('signup')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('signup')  

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your AUTH System ID has been successfully created")
        return redirect('login')

    else:
        return HttpResponse("404 - Not found")     

def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return HttpResponse("404- Not found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')        