from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from traffic import settings

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', obtain_auth_token),
    path('api/', include('traffic.app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
