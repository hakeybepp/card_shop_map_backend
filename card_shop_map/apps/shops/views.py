from rest_framework import viewsets

from .models import Shop
from .serializers import ShopSerializer

class ShopReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShopSerializer

    def get_queryset(self):
        queryset = Shop.objects.all()
