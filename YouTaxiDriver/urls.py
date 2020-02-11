from django.urls import path
from .import views

urlpatterns = [
    path('demo/', views.DemoDriver, name=""),
    path('update/<slug:slug>/', views.UpdateDriver, name=""),
    path('update/byadmin/<slug:slug>/', views.UpdateDriverByAdmin, name=""),
    # path('getdriver/<slug:slug>/', views.GetDriverById, name=""),
    path('mobile/login/', views.DriverMobileLogin, name=""),
    path('validate/otp/', views.DriverMobileValidateOtp, name=""),
    path('resend/otp/',views.DriverMobileResendOtp,name=""),
]