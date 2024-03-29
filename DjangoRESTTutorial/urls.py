from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from DjangoRESTTutorial.quickstart import views
from django.conf.urls.static import static
from DjangoRESTTutorial import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.STATIC_URL)
