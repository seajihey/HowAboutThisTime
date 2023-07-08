from django.urls import path
from .views import *

urlpatterns = [
    # users (모든 유저들을 read / 유저 한 명을 create)
    path("users/", UserList.as_view()),
    # user (특정 유저에 대해 read/update/delete)
    path("user/<pk>/", UserDetail.as_view()),
    path("user/update/<pk>/", UserUpdate.as_view()),
    path("user/delete/<pk>/", UserDelete.as_view()),
    # groups (모든 그룹들을 read / 그룹 한 개를 create)
    path("groups/", GroupList.as_view()),
    # group (특정 그룹에 대해 read/update/delete)
    path("group/<pk>/", GroupDetail.as_view()),
    path("group/update/<pk>/", GroupUpdate.as_view()),
    path("group/delete/<pk>/", GroupDelete.as_view()),
    # image (특정 그룹에 대해 시간표 다운로드)
    path("group/image/<pk>/", GroupImage.as_view()),
]
