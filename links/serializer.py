from rest_framework import serializers
from.models import links

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = links
        fields = "__all__"