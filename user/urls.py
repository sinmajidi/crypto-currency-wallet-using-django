
from django.urls import path,include
from .views import Signin,Signup,User_info,Logout,start_invesment

urlpatterns = [
    path('login', Signin.as_view(),name='signin'),
    path('register', Signup.as_view(),name='register'),
    path('info', User_info.as_view(),name='User_info'),
    path('logout', Logout.as_view(),name='logout'),
    path('start-investment', start_invesment.as_view(),name='start_invesment'),
]
