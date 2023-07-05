from django.shortcuts import render,redirect
from . models import Employeedetails 
from . forms import Employeeform 

def details(request):
    emp_details = Employeedetails.objects.all()
    return render(request,'details.html',{'Employee':emp_details})

def addnew(request):
    form = Employeeform()
    if request.method =='POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/details')
    return render(request,'form.html',{'form':form})

def edit(request,id):
    employee = Employeedetails.objects.get(id=id)
    form = Employeeform(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/details')
    return render(request,'edit.html',{'emp':employee})

def delete(request,id):
    employee = Employeedetails.objects.get(id=id)
    employee.delete()
    return redirect('/details')
