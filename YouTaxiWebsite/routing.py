# from django.urls import re_path
from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/user/', consumers.UserConsumer),
    path('ws/driver/', consumers.UserConsumer),

]