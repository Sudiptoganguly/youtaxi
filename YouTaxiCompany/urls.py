from django.urls import path
from .import views


urlpatterns = [
    path('create/', views.CreateCompany, name=""),
    path('show/list/', views.GetCompanyForTableDispaly),
    
]