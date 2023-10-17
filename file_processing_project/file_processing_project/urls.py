from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import openapi, get_schema_view


from file_processing.views import FileViewSet



router = DefaultRouter()
router.register(r'files', FileViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
    path('upload/', FileViewSet.as_view({'post': 'upload'}), name='file-upload'),

]