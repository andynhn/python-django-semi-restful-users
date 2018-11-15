from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    print("*"*25, "INDEX METHOD", "*"*25)
    context = {
        "all_users": User.objects.all()
    }
    print("*"*25, "END INDEX METHOD", "*"*25)
    return render(request, 'semirestful_users_app/index.html', context)


def new(request):
    print("*"*25, "NEW METHOD", "*"*25)
    print("*"*25, "END NEW METHOD", "*"*25)
    return render(request, 'semirestful_users_app/new.html')  

def edit(request, number):
    print("*"*25, "EDIT METHOD", "*"*25)
    context = {
        "user": User.objects.get(id=number)
    }
    print("*"*25, "END EDIT METHOD", "*"*25)
    return render(request, 'semirestful_users_app/edit.html', context)  


def show(request, number):
    print("*"*25, "SHOW METHOD", "*"*25)
    context = {
        "user": User.objects.get(id=number)
    }

    print("*"*25, "END SHOW METHOD", "*"*25)
    return render(request, 'semirestful_users_app/show.html', context)  


def create(request):
    print("*"*25, "CREATE METHOD", "*"*25)
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            print("*"*25, "END CREATE METHOD", "*"*25)
            return redirect('/users/new')
        else:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            user = User.objects.last()
            number = user.id
            print("*"*25, "END CREATE METHOD", "*"*25)
            return redirect('/users/'+str(number))
    
    else:
        print("*"*25, "END CREATE METHOD", "*"*25)
        return redirect('/users/new')
    

def destroy(request, number):
    print("*"*25, "DESTROY METHOD", "*"*25)
    x = User.objects.get(id=number)
    x.delete()
    print("*"*25, "END DESTROY METHOD", "*"*25)
    return redirect('/users')


def update(request):
    print("*"*25, "UPDATE METHOD", "*"*25)
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            print("*"*25, "END UPDATE METHOD", "*"*25)
            return redirect('/users/'+str(request.POST['number'])+'/edit')
        else:
            user = User.objects.get(id = int(request.POST['number']))
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            print("*"*25, "END UPDATE METHOD", "*"*25)
            return redirect('/users/'+str(request.POST['number']))
    print("*"*25, "END UPDATE METHOD", "*"*25)
    return redirect('/users/'+str(request.POST['number']))