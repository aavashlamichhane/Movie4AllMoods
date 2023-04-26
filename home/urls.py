from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.logIn,name='Log In'),
    path('signup/',views.signUp,name='Sign Up'),
    path('help/',views.help,name='Help'),
    path('aboutUs/',views.aboutUs,name='About Us'),
    path('logout/',views.signout,name='logout'),
]
