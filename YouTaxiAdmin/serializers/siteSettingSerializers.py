from rest_framework import serializers
from ..models import Setting as SiteSetting


class CreateSiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ['paypalEmail', 'siteEmail', 'mobile', 'skype', 'siteName', 'address', 'iconFile', 'logoFile']



class GetSiteSettingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ['paypalEmail', 'siteEmail', 'mobile', 'skype', 'siteName', 'address', 'iconFile', 'logoFile']