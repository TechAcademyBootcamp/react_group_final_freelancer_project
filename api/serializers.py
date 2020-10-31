from rest_framework import serializers
from accounts.models import CustomUser,Skill
from home.models import Project
from inbox.models import Group,Message
from home.models import Project,Level,New,PriceType




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

class SkillSearializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=(
            'id',
            'tag'
        )
class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PriceType
        fields=(
            'id',
            'price_type'
        )
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    skills=SkillSearializer(many=True)
    level=LevelSerializer()
    class Meta:
        model = Project
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('seen',)



        
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

