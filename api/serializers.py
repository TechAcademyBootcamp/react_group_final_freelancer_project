from rest_framework import serializers
from accounts.models import CustomUser
from inbox.models import Group,Message
from home.models import Project




class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model=CustomUser
        fields=(
            'id',
            'first_name',
            'last_name',
            'image',
            'title',
            'overview',
            'hourly_price',   
        )


class MessagesSerializer(serializers.ModelSerializer):
    class Meta():
        model=Message
        fields=(
            'id',
            'text',
            'sender',
            'group',
            'created_at',
        )


class GroupSerializer(serializers.ModelSerializer):
    messages=MessagesSerializer(many=True, read_only=True)
    class Meta():
        model=Group
        fields=(
            'id',
            'messages',
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta():
        model=Project
        fields=(
            'id',
            'description',
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

