from django.urls import path
from app.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


router.register('Customer',CustomerModelViewSet)
router.register('Order',OrderModelViewSet)
router.register('OrderItem',OrderItemModelViewSet)
router.register('Product',ProductModelViewSet)
router.register('Category',CategoryModelViewSet)

urlpatterns = router.urls
