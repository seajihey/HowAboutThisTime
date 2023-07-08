import os, cv2

from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from rest_framework.generics import *

from .models import User, Group
from .serializers import UserSerializer, GroupSerializer
from .table_detection import TableDetector
from .opencv_draw_picture import Drawer

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = BASE_PATH[: BASE_PATH.find("w2m") - 1]


""" 메인 페이지 """


def main(request):
    return render(request, "main.html")


""" RESTful API (CRUD) for User """


# CREATE User
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# READ User(s)
class UserDetail(RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,) # 토큰인증은 ... 넣/말 고민중
    queryset = User.objects.all()
    serializer_class = UserSerializer


# UPDATE User
class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# DELETE User
class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


""" RESTful API (CRUD) for Group """


# CREATE Group
class GroupList(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_instance = User.objects.get(id=request.data["group_users"])
        group_instance = Group.objects.get(group_code=serializer.data["group_code"])

        user_instance.belonging_groups.add(serializer.data["group_code"])
        group_instance.group_users.add(user_instance.id)

        user_instance.save("create_group")
        unavailable_datetimes = {
            "mon": dict(),
            "tue": dict(),
            "wed": dict(),
            "thu": dict(),
            "fri": dict(),
            "sat": dict(),
            "sun": dict(),
        }

        if user_instance.img_path:
            unavailable_datetimes = TableDetector.getUnavailableDatetime(
                user_instance.img_path, unavailable_datetimes, user_instance.id
            )

        group_instance.group_unavailable_datetimes = unavailable_datetimes
        group_instance.save()

        return JsonResponse(
            {
                "group_name": group_instance.group_name,
                "group_code": group_instance.group_code,
                "group_users": [user.id for user in group_instance.group_users.all()],
                "group_unavailable_datetimes": group_instance.group_unavailable_datetimes,
            }
        )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# READ Group
class GroupDetail(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# UPDATE Group
class GroupUpdate(UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True

        group_instance = self.get_object()
        user_instance = User.objects.get(id=request.data["group_users"])

        group_instance.group_users.add(user_instance.id)
        user_instance.belonging_groups.add(group_instance.group_code)

        user_instance.save("update_group")

        if user_instance.img_path:
            group_instance.group_unavailable_datetimes = (
                TableDetector.getUnavailableDatetime(
                    user_instance.img_path,
                    group_instance.group_unavailable_datetimes,
                    user_instance.id,
                )
            )

        group_instance.save()

        return JsonResponse(
            {
                "group_name": group_instance.group_name,
                "group_code": group_instance.group_code,
                "group_users": [user.id for user in group_instance.group_users.all()],
                "group_unavailable_datetimes": group_instance.group_unavailable_datetimes,
            }
        )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# DELETE Group
class GroupDelete(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# DOWNLOAD GroupImage
class GroupImage(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        group_instance = self.get_object()

        time_table_image = Drawer.getImageFromTimeTableDictionary(
            group_instance.group_unavailable_datetimes, "group"
        )

        file_path = BASE_PATH + "/group_images/" + group_instance.group_code + ".png"
        cv2.imwrite(file_path, time_table_image)

        return FileResponse(
            open(file_path, "rb"), content_type="image/png", as_attachment=True
        )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
