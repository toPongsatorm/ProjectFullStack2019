from django.urls import path
from .views import auth_page, home, logoutView ,add_book

app_name = 'example_app'

urlpatterns = [
    path('', home, name='home'),
    path('auth_page/', auth_page, name='auth_page'),
    path('logout/', logoutView, name='logout'),
    path('add/',add_book, name="add_book"),
   
]
