from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('login/',views.logIn,name='Log In'),
    path('signup/',views.signUp,name='Sign Up'),
    path('help/',views.help,name='Help'),
    path('aboutus/',views.aboutus,name='About Us'),
    path('logout/',views.signout,name='Log Out'),
    path('recommend/',views.recommend,name='Recommended Movies'),
    path('filter/',views.filter,name='Advanced Filters'),
    path('userprofile/',views.userprofile,name='UserProfile'),
    path('list/',views.list,name='List'),
    path('p2w/',views.p2w,name='Plan-to-watch')
]
