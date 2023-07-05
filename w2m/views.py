from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status

from .models import User, Group
from .serializers import UserSerializer, GroupSerializer

from .table_detection import TableDetector


##페이지##
def main(request):
    return render(request, "main.html")


#### restapi ####
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,) # 토큰인증은 ... 넣/말 고민중
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        instance = User.objects.get(id=request.data["group_users"])
        instance.belonging_groups.add(serializer.data["group_code"])
        if instance.img_path is not None:
            unavailable_datetimes = TableDetector.getUnavailableDatetime(
                [instance.img_path]
            )
            group_instance = Group.objects.get(group_code=serializer.data["group_code"])
            group_instance.group_unavailable_datetimes = unavailable_datetimes
            group_instance.save()
        instance.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupUpdate(UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        user_instance = User.objects.get(id=request.data["group_users"])
        instance.group_users.add(user_instance)

        user_instance.belonging_groups.add(instance.group_code)
        user_instance.save()

        if user_instance.img_path is not None:
            unavailable_datetimes = TableDetector.getUnavailableDatetime(
                [user_instance.img_path]
            )

            # 덮어쓰기 아니고 리스트 append해야함 #
            instance.group_unavailable_datetimes = unavailable_datetimes

        instance.save()

        # if instance.img_path is not None:
        #     unavailable_datetimes = TableDetector.getUnavailableDatetime(
        #         [instance.img_path]
        #     )
        #     group_instance = Group.objects.get(group_code=serializer.data["group_code"])
        #     group_instance.group_unavailable_datetimes = unavailable_datetimes
        #     group_instance.save()

        return JsonResponse(
            {
                "group_code": instance.group_code,
                "group_name": instance.group_name,
                "group_users": [user.id for user in instance.group_users.all()],
            }
        )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDelete(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
