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
    path('userprofile/',views.profile,name='UserProfile'),
    path('list/',views.lists,name='List'),
    path('p2w/',views.p2w,name='Plan-to-watch'),
    path('search/',views.search,name='Search'),
    path('watched/',views.watched,name='Already Watched'),
    path('alwat/',views.alwat,name='Already Watched button'),
    path('updaterating/',views.updaterating,name="update rating"),
    path('deletelistentry/',views.deleteListEntry,name="delete list entry"),
    path('updatestatus/',views.updateStatus,name="updatestatus")
]
