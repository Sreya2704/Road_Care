from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from tickets.seriaizers import UserSerializer,IssueSerializer
from tickets.models import RoadIssue
from rest_framework import authentication,permissions
from rest_framework.response import Response
from tickets.permissions import IsOwner

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class IssueCreateListView(CreateAPIView,ListAPIView):

    serializer_class=IssueSerializer
    queryset=RoadIssue.objects.all()

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
    
    def get(self,request,*args,**kwargs):
        qs=RoadIssue.objects.filter(reported_by=request.user)
        serializer_instance=IssueSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
class IssueRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=IssueSerializer
    queryset=RoadIssue.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[IsOwner]