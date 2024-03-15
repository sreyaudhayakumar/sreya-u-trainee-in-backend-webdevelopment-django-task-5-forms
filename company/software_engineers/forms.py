from django import forms
from .models import MiddleEmployee
from .models import UploadedFile

class HighEmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    department = forms.CharField(max_length=250)
    yearofjoin = forms.IntegerField()


class MiddleEmployeeForm(forms.ModelForm):
    class Meta:
        model = MiddleEmployee
        fields = ['name', 'age', 'department', 'yearofjoin']


class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']