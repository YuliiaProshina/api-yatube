from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')


router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='post-comments'
)

urlpatterns = [
    path('', include(router.urls)),
]
