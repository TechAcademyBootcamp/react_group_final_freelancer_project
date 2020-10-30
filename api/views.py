from django.shortcuts import render 
from home.models import Project
from accounts.models import Skill
from rest_framework import filters
from rest_framework import generics
from api.serializers import *
from api.filters import DynamicSearchFilter

from rest_framework.response import Response

# Create your views here.
class SearchAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Project.objects.all()
    serializer_class = SearchSerializer  
    search_fields = ["title", "description","price_min","price_max"]
    
    def get_queryset(self):
        
        queryset = Project.objects.all()
        price_min=self.request.query_params.get('price_min',None)  
        price_max=self.request.query_params.get('price_max',None)    
        price_type=self.request.query_params.get('price_type',None)
        skills=self.request.query_params.get('skills',None)
        level=self.request.query_params.get('level',None)
        price_type=self.request.query_params.get('price_type',None)
        print(price_type)
        print(level)
        search=self.request.query_params.get('search',None)
        # title = self.request.query_params.get('title', None)
        if search:
            queryset=queryset.filter(title__icontains=search)

        if price_min:
            queryset=queryset.filter(price_min__gte=price_min)
            print(queryset)
        if price_max:
            queryset=queryset.filter(price_max__lte=price_max)
        if level:
            queryset=queryset.filter(level__id=level)
        if price_type:
            queryset=queryset.filter(price_type__id=price_type)
  

        return queryset

class TagsInputView(generics.ListCreateAPIView):
    serializer_class = SkillSearializer
    queryset = Skill.objects.all()
    # def get_queryset(self):
        
    #     tag=self.request.query_params.get('tag',None)  

    #     if tag:
    #         queryset = Skill.objects.all()
    #         return queryset

