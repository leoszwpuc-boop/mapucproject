from django.contrib import admin
from django.urls import path
from mapucapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home2, name='home'),
    path('movies/new/', movie_create, name='movie_create'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie_delete'),
    path('registro/', registrar, name='registro'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]