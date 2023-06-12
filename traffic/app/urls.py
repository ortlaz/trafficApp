from django.urls import path

from traffic.app.views import (
    LocationsListView,
    LocationsView,
    LoginView,
    UserView,
    ContractList,
    CameraSelectList,
    LocationReportView, ReportCreateView
)

app_name = "app"

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),
    path('contracts', ContractList.as_view(), name='contracts'),
    path('camera-select', CameraSelectList.as_view(), name='camera-select'),
    path('location/list', LocationsListView.as_view(), name='locations-list'),
    path('location/<str:pk>/reports', LocationReportView.as_view(), name='locations-report'),
    path('location/<str:pk>', LocationsView.as_view(), name='locations-update'),
    path('reports', ReportCreateView.as_view(), name='report-create')
]

url_descriptions = {
    'locations-list': {
        "description": "Список локаций"
    }
}
