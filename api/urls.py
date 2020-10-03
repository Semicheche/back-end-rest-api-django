from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)
router.register(r'kits', views.KitsViewSet)

urlpatterns = [
    path('', include(router.urls)),

]