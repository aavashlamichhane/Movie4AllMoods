from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing,name='Landing Page'),
    path('home/',views.index,name='Home'),
    path('home/login/',views.logIn,name='Log In'),
    path('home/signup/',views.signUp,name='Sign Up'),
    path('home/help/',views.help,name='Help'),
    path('home/aboutus/',views.aboutus,name='About Us'),
    path('home/logout/',views.signout,name='Log Out'),
    path('home/recommend/',views.recommend,name='Recommended Movies'),
    path('home/filter/',views.advfilter,name='Advanced Filters'),
    path('home/userprofile/',views.profile,name='UserProfile'),
    path('home/list/',views.lists,name='List'),
    path('home/p2w/',views.p2w,name='Plan-to-watch'),
    path('home/search/',views.search,name='Search'),
    path('home/watched/',views.watched,name='Already Watched'),
    path('home/alwat/',views.alwat,name='Already Watched button'),
    path('home/updaterating/',views.updaterating,name="update rating"),
    path('home/deletelistentry/',views.deleteListEntry,name="delete list entry"),
    path('home/updatestatus/',views.updateStatus,name="updatestatus"),
    path('home/moviedes/<str:title>/', views.moviedes, name='Movie Description')

]