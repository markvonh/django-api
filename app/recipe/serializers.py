from rest_framework import serializers
from .models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the Tag model"""

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ("id",)


class IngredientSerializer(serializers.ModelSerializer):
    """ Serializer for the ingrediant objects """

    class Meta:
        model = Ingredient
        fields = ("id", "name")
        read_only_fields = ("id",)
