from django.shortcuts import render, redirect
from .forms import HighEmployeeForm
from .models import HighEmployee,MiddleEmployee
from .forms import MiddleEmployeeForm
from .forms import UploadedFileForm


def add_high_employee(request):
    if request.method == 'POST':
        form = HighEmployeeForm(request.POST)
        if form.is_valid():

            HighEmployee.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                department=form.cleaned_data['department'],
                yearofjoin=form.cleaned_data['yearofjoin']
            )
            return redirect('success_page')
    else:
        form = HighEmployeeForm()
    return render(request, 'add_high_employee.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')


def add_middle_employee(request):
    if request.method == 'POST':
        form = MiddleEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = MiddleEmployeeForm()
    return render(request, 'add_middle_employee.html', {'form': form})


def list_high_employees(request):
    high_employees = HighEmployee.objects.all()
    return render(request, 'list_high_employees.html', {'high_employees': high_employees})

def list_middle_employees(request):
    middle_employees = MiddleEmployee.objects.all()
    return render(request, 'list_middle_employees.html', {'middle_employees': middle_employees})


def upload_file(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_uploaded_files')
    else:
        form = UploadedFileForm()
    return render(request, 'upload_file.html', {'form': form})

from .models import UploadedFile

def list_uploaded_files(request):
    uploaded_files = UploadedFile.objects.all()
    return render(request, 'list_uploaded_files.html', {'uploaded_files': uploaded_files})

