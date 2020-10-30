from rest_framework.viewsets import ModelViewSet
from accounts.models import CustomUser
from home.models import Project,Skill

from inbox.models import Group,Message
from api.serializers import ProfileSerializer,GroupSerializer, ProjectSerializer, MessagesSerializer,SkillSearializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset. 
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):        
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class


class ProfileViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,]
    serializer_class=ProfileSerializer
    queryset=CustomUser.objects.all()
    http_method_names = ['patch']

    def patch(self, request, pk):
        print("ASDDSADASDSADDAS")
        testmodel_object = self.get_object(pk)
        serializer = TestModelSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

class MessagesViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,]
    serializer_class=GroupSerializer
    queryset=Group.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        queryset = super(MessagesViewSet, self).get_queryset()
        user=self.request.user
        # print(queryset)
        queryset=queryset.filter(users=user)
        # print(queryset)
        # queryset=queryset.filter()
        return queryset 
    
class EditProjectViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated,]
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    http_method_names = ['patch']

    def get_queryset(self):
        queryset = super(EditProjectViewSet, self).get_queryset()
        user=self.request.user
        print(queryset)
        print(queryset.filter(author=user))
        queryset=queryset.filter(author=user)
        # queryset=queryset.filter()
        return queryset
    
    # def patch(self, request, pk):
    #     testmodel_object = self.get_object(pk)
    #     serializer = ProjectSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
    #     print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    #     print(serializer.data)
    #     if 
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(code=201, data=serializer.data)
    #     return JsonResponse(code=400, data="wrong parameters")
    def update(self, request, *args, **kwargs):
        id=kwargs['pk']
        user=self.request.user
        project=Project.objects.get(id=id)

        if project.author != user:
            error_msg = 'It is not your project'
            return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)

        if project.status == 2:
            error_msg = "You can't change completed Project description"
            return Response({'error': error_msg}, status=status.HTTP_400_BAD_REQUEST)

        return super(EditProjectViewSet,self).update(request, *args, **kwargs)


# class SubscribeViewSet(ModelViewSet):
#     queryset=Subscribe.objects.all()
#     http_method_names=['post']
#     serializer_class=SubscribeSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         # serializer.data["Success"]="Email is added succesfully!"
#         self.newdict={"success":"Email is added succesfully!"}
#         self.newdict.update(serializer.data) 
#         return Response(self.newdict, status=HTTP_201_CREATED, headers=headers)


    

