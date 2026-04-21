from rest_framework.routers import DefaultRouter
from .views import WorkspaceMemberViewSet
from .views import (
    WorkspaceViewSet,
    WorkspaceMemberViewSet,
    DocumentViewSet,
    CommentViewSet,
    TagViewSet,
    AuditLogViewSet
)

router = DefaultRouter()
router.register('workspaces', WorkspaceViewSet)
router.register('members', WorkspaceMemberViewSet)
router.register('documents', DocumentViewSet)
router.register('comments', CommentViewSet)
router.register('tags', TagViewSet)
router.register('auditlogs', AuditLogViewSet)

urlpatterns = router.urls
