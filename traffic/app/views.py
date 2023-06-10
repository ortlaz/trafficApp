from django.contrib.auth import login
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from traffic.app.models import Location
from traffic.app.serializers import LocationsListSerializers, LoginSerializer, UserSerializer


# Users
# __________________________________________________________________________________
class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


# __________________________________________________________________________________

# Locations
# __________________________________________________________________________________
class LocationsListView(ListCreateAPIView):
    """Список и создание локаций"""
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationsListSerializers
    queryset = Location.objects.all()


class LocationsView(RetrieveUpdateAPIView):
    """Просмотр и обновление локации"""
    serializer_class = LocationsListSerializers
    queryset = Location.objects.all()
    permission_classes = []
