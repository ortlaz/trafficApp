from django.urls import path

from traffic.app.views import LocationsListView, LocationsView, LoginView, UserView, ContractList, CameraSelectList

app_name = "app"

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),
    path('contracts', ContractList.as_view(), name='contracts'),
    path('camera-select', CameraSelectList.as_view(), name='camera-select'),
    path('location/list', LocationsListView.as_view(), name='locations-list'),
    path('location/<str:pk>', LocationsView.as_view(), name='locations-update')
]

url_descriptions = {
    'locations-list': {
        "description": "Список локаций"
    }
}
