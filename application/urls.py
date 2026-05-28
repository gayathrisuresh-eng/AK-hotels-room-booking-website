from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'), 
    path('rooms/',views.rooms,name='rooms'),
    path('book/<int:room_id>/',views.book_room,name='book_room'),
]
