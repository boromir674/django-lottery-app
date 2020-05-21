from rest_framework import routers
from .views.api import BusinessesViewSet
from .views.product import ProductViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'businesses', BusinessesViewSet, 'business')
router.register(r'products', ProductViewSet, 'product')

urlpatterns = router.urls

# urlpatterns = [
#     path('business_admin/', dj_admin.site.urls),
#     # path('api/', include('rest_framework.urls', namespace='rest_framework')),
# ]
