from django.urls import include, path
from rest_framework_nested import routers
from . import views
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet,basename='products')
router.register('collections', views.collectionViewSet,basename='collections')
router.register('carts', views.CartViewSet)
products_router = routers.NestedDefaultRouter(router,'products',lookup='product')
products_router.register('reviews', views.ReviewViewSet,basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router,'carts',lookup='cart')
carts_router.register('items', views.CartItemViewSet,basename='cart-items')
# URLConf
urlpatterns = [
    path('',include(router.urls)),
    path('',include(products_router.urls)),
    path('',include(carts_router.urls)),
]
