from rest_framework import generics
from python_app.models import Device, Reading
from python_app.serializers import DeviceSerializer, ReadingSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

'''
API необходимо реализовать с помощью Django Rest Framework, авторизовать запросы не нужно:
Для создания API использовал generic class-based views
Запросы авторизировал, т.к. привязал пользователя
'''

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

# Возвращать пользователю список доступных для него приборов учета (методом GET)

class UserDeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        queryset = self.get_queryset()
        user = self.request.user
        queryset = queryset.filter(user_id=user)
        return Response(DeviceSerializer(queryset, many=True).data)

class DeviceDetail(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticated,)

# Предоставлять пользователю возможность передачи показаний по конкретному прибору учета (методом POST)

class ReadingList(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'device_id': serializer.validated_data['device_id'].device_id,
                             'value': serializer.validated_data['value']}, status=status.HTTP_201_CREATED, headers=headers)
        return Response({
            'status': 'Bad request',
            'message': 'Reading could not be created with received data'
        }, status=status.HTTP_400_BAD_REQUEST)

class ReadingDetail(generics.RetrieveAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = (permissions.IsAuthenticated,)

