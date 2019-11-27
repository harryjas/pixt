from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /register/
    path('register/', views.register, name='register'),
    # /music/
    path('music/', views.index, name='index'),
    # /music/<album_id>/
    path('music/<int:album_id>/', views.detail, name='detail'),
    # /music/album/add/
    path('music/album/add/', views.create_album, name='album-add'),
    # /music/album/<album_id>/
    path('music/album/<int:album_id>/', views.update_album, name='album-update'),
    # /logout/
    path('logout/', views.logout_user, name='logout'),
    # /login/
    path('', views.login_user, name='login'),
    # /music/<album_id>/delete_album/
    path('music/<int:album_id>/delete_album/', views.delete_album, name='delete_album'),
    # /music/<album_id>/create_song/
    path('<int:album_id>/create_song/', views.create_song, name='create_song'),
    # /music/<album_id>/delete_song/<song_id>/
    path('<int:album_id>/delete_song/<int:song_id>', views.delete_song, name='delete_song'),
    # /music/songs/( )/
    path('songs/<slug:filter_by>/', views.songs, name='songs'),
    # /music/create_album/
    path('create_album/', views.create_album, name='create_album'),

]
