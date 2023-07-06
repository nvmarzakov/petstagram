from django.urls import path

from petstagram_workshop.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
