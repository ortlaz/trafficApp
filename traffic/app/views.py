from django.contrib.auth import login
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from traffic.app.models import Location, Camera, Report
from traffic.app.serializers import LocationsListSerializers, LoginSerializer, UserSerializer, ContractSerializer, \
    CameraSelectListSerializer, LocationsSerializers, ReportSerializer, ReportUploadSerializer


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


class ContractList(ListAPIView):
    serializer_class = ContractSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationsSerializers
    queryset = Location.objects.all()


class LocationReportView(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = ReportSerializer

    def get_queryset(self):
        location_id = self.kwargs.get('pk')
        return Report.objects.filter(location_id=location_id)


class CameraSelectList(ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = CameraSelectListSerializer
    queryset = Camera.objects.all()


class ReportCreateView(ListCreateAPIView):
    serializer_class = ReportUploadSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
