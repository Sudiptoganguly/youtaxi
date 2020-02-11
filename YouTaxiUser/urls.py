from django.urls import path
from .import views

urlpatterns = [
    path('demo/', views.DemoUser, name=""),
    path('registration/', views.ClientRegistration, name=""),
    path('login/',views.ClientLogin,name=""),
    path('update/', views.Update, name=""),
    path('validate/otp/', views.ValidateOTP, name=""),
    path('resend/otp/',views.UserMobileResendOtp,name=""),
    path('request/', views.UserRequest, name=""),
]