from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from crud.forms import EmployeeForm
from crud.models import Employee
from crud.models import Login
from .models import Drop
from .models import Dropform
from django.contrib.sessions.models import Session

# Create your views here.
def login(request,):
    if request.method == "POST":
      loginemail = request.POST['email']
      loginpass = request.POST['password']
      user = Login.objects.get(email=loginemail, password=loginpass)
      if user is not None:
        request.session['islogin'] = True
        return redirect('/show')
      else:
        return redirect('/login')
    return render(request,"login.html")

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
              pass
    else:
        form = EmployeeForm()
    return render(request,"index.html",{'form':form})

def show(request):

     employees = Employee.objects.all()
     if request.session.has_key('islogin'):
      return render(request,"show.html",{'employee':employees})

def edit(request,id):
    employees = Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee':employees})
def update(request,id):
    employees = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance = employees)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html",{'employee':employees})
def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def drop(request):
    drop = Drop.objects.all().order_by('id')
    return render(request,'dropdown.html',{'drop':drop})

def add(request):
    if (request.POST):
        data = request.POST.dict()
        del data["csrfmiddlewaretoken"]
        new_request = Dropform.objects.create(**data)
        new_request.save()

