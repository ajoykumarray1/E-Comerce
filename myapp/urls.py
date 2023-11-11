from django.urls import path,include
from myapp.views import *
urlpatterns = [
    
    path('', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('home/', home, name='home'),
    path('logout', logoutpage, name='logout'),
    
]
