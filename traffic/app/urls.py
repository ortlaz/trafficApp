from django.urls import path

from traffic.app.views import LocationsListView, LocationsView, LoginView, UserView

app_name = "app"

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('user', UserView.as_view(), name='user'),
    path('location/list', LocationsListView.as_view(), name='locations-list'),
    path('location/<str:pk>', LocationsView.as_view(), name='locations-list')
]

url_descriptions = {
    'locations-list': {
        "description": "Список локаций"
    }
}
