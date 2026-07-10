from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "category",
            "category_name",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]