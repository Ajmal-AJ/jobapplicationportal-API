from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, ApplicationViewSet, UserApplicationsAPIView
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

app_name ='api'

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Job Application API",
        default_version='v1',
        description="API documentation for Job and Application models",
        terms_of_service="https://jobportalapi.ajmalaj.com/api",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', include(router.urls)),
    path('user-applications/', UserApplicationsAPIView.as_view(), name='user-applications'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]