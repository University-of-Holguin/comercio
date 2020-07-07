from django.urls import include, path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .viewsets import (
    OficodaViewset,
    RepartoViewset,
    BodegaViewset,
    DistribucionViewset,
    ProductoViewset,
)

router = routers.DefaultRouter()
router.register(r"oficoda", OficodaViewset)
router.register(r"reparto", RepartoViewset)
router.register(r"bodega", BodegaViewset)
router.register(r"distribucion", DistribucionViewset)
router.register(r"producto", ProductoViewset)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]