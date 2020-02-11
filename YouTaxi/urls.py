from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('website/', include('YouTaxiWebsite.urls')),
    path('admin/', include('YouTaxiAdmin.urls')),
    path('user/', include('YouTaxiUser.urls')),
    path('driver/', include('YouTaxiDriver.urls')),
    path('company/', include('YouTaxiCompany.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)