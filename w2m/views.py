from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import *

from .models import User, Group
from .serializers import UserSerializer, GroupSerializer


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
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupUpdate(UpdateAPIView):
    def patch(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        instance.group_users.add(User.objects.get(id=request.data["group_users"]))
        instance.save()

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
