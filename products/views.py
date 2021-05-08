from rest_framework.viewsets import ModelViewSet

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer
from .permissions import IsProductUserOrReadOnly


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsProductUserOrReadOnly, )

class ProductCategoryView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (IsProductUserOrReadOnly, )