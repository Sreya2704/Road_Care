from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from tickets.seriaizers import UserSerializer,IssueSerializer,CommentSerializer
from tickets.models import RoadIssue,Comment
from rest_framework import authentication,permissions
from rest_framework.response import Response
from tickets.permissions import IsOwner,IsCommentOwner

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class IssueCreateListView(CreateAPIView,ListAPIView):

    serializer_class=IssueSerializer
    queryset=RoadIssue.objects.all()

    #authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
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
    #authentication_classes=[authentication.BasicAuthentication]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

class CommentCreateView(CreateAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        id=self.kwargs.get("pk")
        issue_obj=RoadIssue.objects.get(id=id)
        serializer.save(user=self.request.user,issue=issue_obj)

class CommentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsCommentOwner]
    