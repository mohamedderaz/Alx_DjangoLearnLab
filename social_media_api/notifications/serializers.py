from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField(read_only=True)  # مين عمل الأكشن
    recipient = serializers.StringRelatedField(read_only=True)  # مين وصله الإشعار
    target_object = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_object', 'timestamp', 'is_read']

    def get_target_object(self, obj):
        if obj.target:
            return str(obj.target)  # بيرجع اسم الـ target بدل ما يدي ID خام
        return None