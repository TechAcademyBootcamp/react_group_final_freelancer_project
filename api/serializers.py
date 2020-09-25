from rest_framework import serializers
from accounts.models import CustomUser



class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model=CustomUser
        fields=(
            'id',
            'title',
            'image',
        )

# class ReadRecipeSerializer(serializers.ModelSerializer):
#     category=CategorySerializer()
#     # tags=TagSerializer()
#     class Meta():
#         model=Recipe
#         fields=(
#             'id',
#             'title',
#             'image',
#             'short_description',
#             'category',
#             'author',
#             'tags',
#         )

