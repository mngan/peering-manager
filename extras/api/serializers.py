from rest_framework import serializers

from extras.models import JobResult, Webhook
from users.api.nested_serializers import UserNestedSerializer
from utils.api.fields import ContentTypeField

from .nested_serializers import *


class JobResultSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="extras-api:jobresult-detail")
    user = UserNestedSerializer(read_only=True)
    obj_type = ContentTypeField(read_only=True)

    class Meta:
        model = JobResult
        fields = [
            "id",
            "url",
            "created",
            "completed",
            "name",
            "obj_type",
            "status",
            "user",
            "data",
            "job_id",
            "output",
        ]


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webhook
        fields = [
            "id",
            "name",
            "type_create",
            "type_update",
            "type_delete",
            "url",
            "enabled",
            "http_method",
            "http_content_type",
            "secret",
            "ssl_verification",
            "ca_file_path",
        ]
