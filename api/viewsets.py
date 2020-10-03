from rest_framework.viewsets import ModelViewSet
from accounts.models import CustomUser
from api.serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
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


    



