from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('login/', views.login_signup, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my-account/', views.myaccount, name='my-account'),
]