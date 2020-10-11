from rest_framework import serializers
from accounts.models import CustomUser,Skill
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

class SkillSearializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=(
            'id',
            'title'
        )



class SearchSerializer(serializers.ModelSerializer):
    skills=SkillSearializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'



        
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

