from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from emp_app.models import Employee, Role, Department
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html")

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"emp_app/view.html",context)
    

def add_emp(request):
    if request.method == "POST":
        fn=request.POST.get('fn')
        ln=request.POST.get('ln')
        dn=request.POST.get('dn')
        bns=request.POST.get('bns')
        role=request.POST.get('role')
        pn=request.POST.get('pn')
        emp=Employee(first_name=fn,last_name=ln,dept_id=dn,bonous=bns,role_id=role,phone=pn,hire_date=datetime.now())
        emp.save()
    return render(request,"emp_app/add.html")

def remove(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Enter Vaild Employe")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"emp_app/remove.html",context)

def filter_emp(request):
    if request.method == 'POST':
        name=request.POST.get('fn')
        dept=request.POST.get('dn')
        role=request.POST.get('role')
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__first_name=dept)
        if role:
            emps=emps.filter(role__role_name=role)

        context = {
            "emps":emps
        }
        return render(request,'emp_app/view.html',context)
    
    return render(request,'emp_app/filter.html')