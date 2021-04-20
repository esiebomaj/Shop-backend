from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),

    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('obtain/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    re_path(r'^', include('django.contrib.auth.urls')),
]
