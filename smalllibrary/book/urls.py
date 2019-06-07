
from django.urls import path
from .views import auth_page,home,logoutView,list_item,sent
app_name = 'book'
urlpatterns = [
    path('', home, name='home'),
    path('auth_page/', auth_page, name='auth_page'),
    path('logout/', logoutView, name='logout'),

    path('sent/<int:pk>',sent,name='sent'),

    #path('sent/<int:pk>',sent,name='sent'),

    path('list',list_item,name='list_item')
 
]
