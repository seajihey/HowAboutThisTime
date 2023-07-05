from django.shortcuts import render
from rest_framework import generics
from .models import User, Group
from .serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


##페이지##
def main(request):
    return render(request, "main.html")


#### restapi ####
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,) # 토큰인증은 ... 넣/말 고민중
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupUpdate(generics.UpdateAPIView):
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
