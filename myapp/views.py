from django.shortcuts import redirect, render
from .forms import signuppage,loginpage
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request,'category.html')


def signup_page(request):
    if request.method=="POST":
        form=signuppage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('signup')
    else:
       form = signuppage
    return render(request, 'signuppage.html', {'form': form})

def login_page(request):
    if request.method=="POST":
        forms=loginpage(request.POST)
        if forms.is_valid():
            usern = forms.cleaned_data['username']
            passw = forms.cleaned_data['password']
            user = authenticate(request, username=usern, password=passw)
            if user:
                login(request,user)
                return redirect('home')
        else:
            return redirect('login')
    else:
        form=loginpage
    return render(request,"loginpage.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect('login')

