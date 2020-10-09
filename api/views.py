from django.shortcuts import render 
from home.models import Project
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
    search_fields = ["title", "description","price_min"]
    
    def get_queryset(self):
        
        queryset = Project.objects.all()
        price_min=self.request.query_params.get('price_min',None)        
        search=self.request.query_params.get('search',None)
        # title = self.request.query_params.get('title', None)
        if search:
            queryset=queryset.filter(title__icontains=search)

        if price_min:
            queryset=queryset.filter(price_min__gte=price_min)
            print(queryset)
        return queryset