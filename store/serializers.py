from . models import Product
from rest_framework import serializers

class ProductSerilizers(serializers.HyperlinkedModelSerializer):
    subcategory = serializers.CharField(source='subcategory_id')
    class Meta:
        model = Product
        fields = '__all__'