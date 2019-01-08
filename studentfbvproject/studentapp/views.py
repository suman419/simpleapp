from django.shortcuts import render,redirect
from studentapp.models import Student
from studentapp.forms import StudentForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from studentapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
@login_required
def employee_view(request):
    employees=Student.objects.all().order_by('-id')

    query=request.GET.get("q")
    if query:
        employees=employees.filter(Q(saddress=query) | Q(sname=query) | Q(sname=query)).distinct()

    paginator=Paginator(employees,5)
    page=request.GET.get('page')
    try:
        employees=paginator.page(page)
    except PageNotAnInteger:
        employees=paginator.page(1)
    except EmptyPage:
        employees=paginator.page(paginator.num_pages)
    context={"employees" : employees,"title":"List"}
    return render(request,'testapp/home.html',{'employees':employees},context)

@login_required
def create_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #message success
            messages.success(request,"Successfully Added")
        return redirect('/')
    else:
        messages.error(request,"Item not Saved")
    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    employee=Student.objects.get(id=id)
    employee.delete()
    #message success
    messages.success(request,"Successfully Deleted")
    return redirect('/')


def update_view(request,id):
    employee=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            #message success
            messages.success(request,"Successfully Updated")
            return redirect('/')
        else:
            messages.error(request,"Item not Updated")
    return render(request,'testapp/update.html',{'employee':employee})


def profile_view(request,id):
    employee=Student.objects.get(id=id)
    return render(request,'testapp/view.html',{'employee':employee})

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
