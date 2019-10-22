from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.views.generic import TemplateView


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('openapi/', TemplateView.as_view(template_name="index.html"))
]