from django.urls import path

from .views import ShopReadOnlyViewSet


urlpatterns = [
    path('shops/', ShopReadOnlyViewSet.as_view())
]
