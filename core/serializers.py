from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag

from .models import (
    Workspace,
    WorkspaceMember,
    Document,
    DocumentVersion,
    Comment,
    Tag,
    AuditLog
)


# 👤 User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# 🏢 Workspace
class WorkspaceSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Workspace
        fields = '__all__'

    # ✅ CUSTOM VALIDATION
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Workspace name too short")
        return value


# 👥 Workspace Member
class WorkspaceMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkspaceMember
        fields = '__all__'


# 📄 Document
class DocumentSerializer(serializers.ModelSerializer):
    versions_count = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = '__all__'

    # ✅ SerializerMethodField
    def get_versions_count(self, obj):
        return obj.versions.count()

    # ✅ VALIDATION
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        return value


# 📄 Document Version
class DocumentVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVersion
        fields = '__all__'


# 💬 Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# 🏷 Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 📜 Audit Log
class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'