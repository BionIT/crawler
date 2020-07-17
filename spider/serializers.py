from rest_framework import serializers
from spider.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'source', 'price', 'userId')