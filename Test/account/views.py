from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer, MemberSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset  = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = ( filters.OrderingFilter,filters.SearchFilter)
    search_fields = ('firstname')


class CreateMemberView(CreateAPIView):
    model=get_user_model()

    permission_classes = (AllowAny,)
    serializer_class = MemberSerializer
