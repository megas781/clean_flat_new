from rest_framework import serializers
from service.models import Order

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    address = serializers.CharField()
    order_date = serializers.DateField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)