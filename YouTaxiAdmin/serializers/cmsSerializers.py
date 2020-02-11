from rest_framework import serializers
from ..models import CMS


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMS
        fields = ['heading', 'pageName', 'content']



class GetCMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMS
        fields = ['id', 'heading', 'pageName', 'content', 'status', 'isDeleted', 'date']