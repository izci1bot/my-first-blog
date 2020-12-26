from django.urls import path
from .views import (
    post_list,
    index
)

urlpatterns = [
    path('', index, name='index'),
    path('post_list/', post_list, name='post_list'),
]

