from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from .permissions import IsUserOrReadOnly


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    permission_classes = (IsUserOrReadOnly, )