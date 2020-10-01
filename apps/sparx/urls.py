from rest_framework import routers
from .views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
urlpatterns = router.urls