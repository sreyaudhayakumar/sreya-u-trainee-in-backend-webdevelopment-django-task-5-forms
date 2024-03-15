from django.urls import path
from.import views

urlpatterns = [
         path('add-high-employee/', views.add_high_employee, name='add_high_employee'),
         path('success/', views.success_page, name='success_page'),
         path('add-middle-employee/',views.add_middle_employee, name='add_middle_employee'),
         path('list-high-employees/', views.list_high_employees, name='list_high_employees'),
         path('list-middle-employees/',views. list_middle_employees, name='list_middle_employees'),
         path('upload/', views.upload_file, name='upload_file'),
         path('list-uploaded-files/', views.list_uploaded_files, name='list_uploaded_files'),
]