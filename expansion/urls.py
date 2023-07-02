
from django.contrib import admin
from django.urls import path,include
from user.views import Signin


urlpatterns = [
    path('', include('greating.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),

]
