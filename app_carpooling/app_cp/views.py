from .models import Trip, User
from .serializers import TripSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import status
from rest_framework import mixins
from rest_framework.response import Response

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TripViewSet(viewsets.GenericViewSet, 
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return [IsAuthenticated(), ]

    def perform_create(self, serializer):
        car_owner = self.request.user.car
        if car_owner is not None:
            place_in_car = self.request.user.car.place_in
            place_in_field = serializer.validated_data
            if place_in_field['place_in_car'] > place_in_car:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(owner=self.request.user)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        return super().create(request)
    

    def list(self, request):
        return super().list(request)