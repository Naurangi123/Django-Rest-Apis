from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCreateView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),  # This will include all the routes from ProductViewSet
    path('create-product/', ProductCreateView.as_view(), name='product-create'),  # Correct path format
]
