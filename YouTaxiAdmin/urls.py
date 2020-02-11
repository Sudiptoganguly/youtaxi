from django.urls import path
from .import views


urlpatterns = [
    path('demo/', views.DemoAdmin, name=""),
    path('create/', views.CreateAdmin, name=""),
    path('get/admin/<slug:slug>/', views.GetAdminData, name=""),
    path('login/', views.AdminLogin, name=""),
    path('create/user/', views.CreateUser, name=""),
    path('create/user/byadmin/', views.CreateUserByAdmin, name=""),
    path('create/driver/', views.CreateDriver, name=""),
    path('create/driver/byadmin/', views.CreateDriverByAdmin, name=""),
    path('fare/create/', views.CreateFare, name=""),
    path('fare/', views.GetAllFares, name=""),
    path('fare/<slug:slug>/', views.GetFareById, name=""),
    path('fare/update/<slug:slug>/', views.UpdateFare, name=""),
    path('create/vehicles/', views.CreateVehicles, name=""),
    path('vehicles/', views.GetAllVehicles, name=""),
    path('vehicles/<slug:slug>/', views.GetVehiclesById, name=""),
    path('update/vehicles/<slug:slug>/', views.UpdateVehicle, name=""),
    path('vehicles-type/', views.GetAllVehicleTypes, name=""),
    path('vehicles-type/<slug:slug>/', views.GetVehicleTypeById, name=""),
    path('create/vehicles-type/', views.CreateVehicleType, name=""),
    path('update/vehicles-type/<slug:slug>/', views.UpdateVehicleType, name=""),
    path('create/cms/', views.CreateCMS, name=""),
    path('cms/', views.GetAllCMS, name=""),
    path('cms/<slug:slug>/', views.GetCMSById, name=""),
    path('create/email-tempalte/', views.CreateEmailTemplate, name=""),
    path('email-tempalte/', views.GetAllEmailTemplates, name=""),
    path('email-tempalte/<slug:slug>/', views.GetEmailTemplateById, name=""),
    path('create/sites-etting/', views.SiteSetting, name=""),
    path('sites-setting/', views.GetSiteSetting, name=""),
    path('user/activate/<slug:slug>/', views.UserActivate, name=""),
    path('user/deactivate/<slug:slug>/', views.UserDeactivate, name=""),
    path('driver/activate/<slug:slug>/', views.DriverActivate, name=""),
    path('driver/deactivate/<slug:slug>/', views.DriverDeactivate, name=""),
    path('user/delete/<slug:slug>/', views.DeleteUser, name=""),
    path('driver/delete/<slug:slug>/', views.DeleteDriver, name=""),
    path('create/car/',views.CreateCar,name=""),
    path('get/car/byadmin/',views.GetAllCarsForAdmin,name=""),
    path('get/car/byothers/',views.GetAllCarsForOthers,name=""),
    path('get/car/byid/<slug:slug>/',views.CarTypeById,name=""),
    path('car/delete/<slug:slug>/',views.CarActivateDactivate,name=""),
    path('car/update/<slug:slug>/',views.CarUpdate,name=""),

    

]