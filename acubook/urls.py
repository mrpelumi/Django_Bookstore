from django.urls import path
from . import views

app_name = 'acubook'
urlpatterns = [
    path('',views.index,name='index'),
    path('bookstore/arts',views.arts,name='arts'),
    path('bookstore/business',views.business,name='business'),
    path('bookstore/christianbooks',views.christian,name='christian'),
    path('bookstore/motivational',views.motivational,name='motivational'),
    path('bookstore/nigerian',views.nigerian,name='nigerian'),
    path('bookstore/science',views.science,name='science'),
    path('bookstore/teenbooks',views.teenbooks,name='teenbooks'),
    path('bookstore/about_us',views.about_us,name='about_us'),
    path('bookstore/register',views.register,name='register'),
    path('bookstore/logout',views.user_logout,name='logout'),
    path('bookstore/user_login',views.user_login,name='user_login'),
    path('bookstore/description',views.description,name='description'),
]
