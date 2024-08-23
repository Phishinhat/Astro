from django.urls import path
from .views import index, register, dashboard, profile_list, profile_image_upload, dweet_image_upload, comment_image_upload, reply_image_upload, profile, dweet, comment, reply, dweet_edit, comment_edit, reply_edit

app_name = 'astro'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile_image_upload/', profile_image_upload, name='profile_image_upload'),
    path('dweet_image_upload/<int:pk>', dweet_image_upload, name='dweet_image_upload'),
    path('comment_image_upload/<int:pk>', comment_image_upload, name='comment_image_upload'),
    path('reply_image_upload/<int:pk>', reply_image_upload, name='reply_image_upload'),
    path('profile/<int:pk>', profile, name='profile'),
    path('dweet/<int:pk>', dweet, name='dweet'),
    path('comment/<int:pk>', comment, name='comment'),
    path('reply/<int:pk>', reply, name='reply'),
    path('dweet_edit/<int:pk>', dweet_edit, name='dweet_edit'),
    path('comment_edit/<int:pk>', comment_edit, name='comment_edit'),
    path('reply_edit/<int:pk>', reply_edit, name='reply_edit'),
]