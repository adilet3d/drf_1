from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
User= get_user_model()
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import action
from mainapp.serializer import CoursesSerializer
from mainapp.models import Courses


class CoursesView(ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer
    @action(methods=['post',], detail=True,\
        serializer_class=CoursesSerializer,permission_classes=\
            (permissions.IsAuthenticatedOrReadOnly))
    def add_course (self , request, *args, **kwargs):
        courses= self.get_object()
        user= request.user
        serializer=CoursesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        course=Courses.objects.create(
            courses=courses,
            name= data.get('name'),
            start_date= data.get('start_date'),
            description= data.get('description'),
            user= user,
        )
        return Response(CoursesSerializer(course).data)
