from rest_framework import serializers
from ..models import EmailTemplate


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ['subject', 'content', 'status']



class GetAllTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ['subject', 'content', 'status', 'isDeleted', 'date']