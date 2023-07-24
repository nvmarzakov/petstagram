from django.urls import path

from petstagram_workshop.common.views import index, like_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>', like_photo, name='like photo')
)
