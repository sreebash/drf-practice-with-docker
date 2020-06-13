from rest_framework import serializers

from restaurants.models import Restaurant, FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'created_on', 'updated_on')
        read_only_field = ('id',)


class RestaurantSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, source='fooditem_set')

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone', 'food_items', 'created_on', 'updated_on')
        read_only_field = ('id',)
