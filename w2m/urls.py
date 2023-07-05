from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path("users/", UserList.as_view()),
    path("user/<pk>/", UserDetail.as_view()),
    path("groups/", GroupList.as_view()),
    path("group/<pk>/", GroupDetail.as_view()),
    path("group/update/<pk>/", GroupUpdate.as_view()),
]
