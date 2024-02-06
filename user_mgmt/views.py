from rest_framework.response import Response
from rest_framework import viewsets, status
from User.models import User
from user_mgmt.serializers import UsersSerializer

class UsersListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'msg': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
    
class UsersDetailViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        return Response(user)
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user, data=request.data, context={'id': 'pk'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Bad Request'}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response({'msg': 'Deleted'}, status=status.HTTP_200_OK)