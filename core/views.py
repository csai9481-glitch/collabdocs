from django.db.models import Q, Count
from rest_framework import viewsets, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import Tag
from .serializers import TagSerializer

from .models import AuditLog
from .serializers import AuditLogSerializer

from .models import Comment
from .serializers import CommentSerializer

from .models import WorkspaceMember
from .serializers import WorkspaceMemberSerializer

from django.db import transaction, IntegrityError
from django.contrib.auth.models import User

from .serializers import (
    DocumentSerializer,
    DocumentVersionSerializer
)

from .models import (
    Workspace,
    WorkspaceMember,
    Document,
    DocumentVersion,
    Comment,
    Tag,
    AuditLog
)

from .serializers import (
    WorkspaceSerializer,
    WorkspaceMemberSerializer,
    DocumentSerializer,
    CommentSerializer,
    TagSerializer,
    AuditLogSerializer
)

# ================= WORKSPACE =================
class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.select_related('owner')
    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                workspace = serializer.save(owner=self.request.user)

                WorkspaceMember.objects.create(
                    workspace=workspace,
                    user=self.request.user,
                    role='admin'
                )

        except IntegrityError:
            raise serializers.ValidationError("User already a member of this workspace")

# ================= DOCUMENT =================
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related(
        'workspace', 'created_by'
    ).prefetch_related('tags')

    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    # ✅ FILTER + SEARCH + Q OBJECT
    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.query_params.get('search')
        status = self.request.query_params.get('status')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    # ✅ AGGREGATION
    @action(detail=False, methods=['get'])
    def stats(self, request):
        total_docs = Document.objects.count()
        draft_docs = Document.objects.filter(status='draft').count()

        return Response({
            "total_documents": total_docs,
            "draft_documents": draft_docs
        })

    # ✅ CUSTOM ACTION - VERSIONS
    @action(detail=True, methods=['get'])
    def versions(self, request, pk=None):
        document = self.get_object()
        versions = document.versions.all()
        serializer = DocumentVersionSerializer(versions, many=True)
        return Response(serializer.data)

    # ✅ TRANSACTION (IMPORTANT)
    def perform_create(self, serializer):
        with transaction.atomic():
            document = serializer.save()

            DocumentVersion.objects.create(
                document=document,
                title=document.title,
                content=document.content,
                version_number=document.versions.count() + 1
            )

    def perform_update(self, serializer):
        with transaction.atomic():
            document = serializer.save()

            DocumentVersion.objects.create(
                document=document,
                title=document.title,
                content=document.content,
                version_number=document.versions.count() + 1
            )# ================= TAGS =================
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


# ================= AUDIT =================
class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.select_related('actor')
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]

# ================= COMMENT =================
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related(
        'document', 'user', 'parent'
    )
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# ================= WORKSPACEMEMBER  =================
class WorkspaceMemberViewSet(viewsets.ModelViewSet):
    queryset = WorkspaceMember.objects.select_related(
        'workspace', 'user'
    )
    serializer_class = WorkspaceMemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save()
        except IntegrityError:
            raise serializers.ValidationError("User already a member of this workspace")