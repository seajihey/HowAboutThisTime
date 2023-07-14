from django.urls import path
from .views import *

urlpatterns = [
    # users (모든 유저들을 read / 유저 한 명을 create)
    path("api/users/", UserList.as_view()),
    # user (특정 유저에 대해 read/update/delete)
    path("api/user/<pk>/", UserDetail.as_view()),
    path("api/user/update/<pk>/", UserUpdate.as_view()),
    path("api/user/delete/<pk>/", UserDelete.as_view()),
    # groups (모든 그룹들을 read / 그룹 한 개를 create)
    path("api/groups/", GroupList.as_view()),
    # group (특정 그룹에 대해 read/update/delete)
    path("api/group/<pk>/", GroupDetail.as_view()),
    path("api/group/update/<pk>/", GroupUpdate.as_view()),
    path("api/group/delete/<pk>/", GroupDelete.as_view()),
    # 그룹 나가기
    path("api/user/exit/<pk>/", UserExit.as_view()),
    # image (특정 그룹에 대해 시간표 다운로드)
    path("api/group/image/<pk>/", GroupImage.as_view()),
]
