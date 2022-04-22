from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name = 'employee_insert'),
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete'),
    path('<int:id>/', views.employee_form, name = 'employee_update'),
    path('list/', views.employee_list, name = 'employee_list')
]