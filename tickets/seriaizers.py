from rest_framework import serializers
from tickets.models import User,RoadIssue,Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password","phone"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class IssueSerializer(serializers.ModelSerializer):

    reported_by=serializers.StringRelatedField(read_only=True)
    comments=serializers.SerializerMethodField(read_only=True)
    comment_count=serializers.SerializerMethodField(read_only=True)
    likes=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=RoadIssue
        fields="__all__"
        read_only_fields=["id","reported_by","created_at","updated_at"]

    def get_comment_count(self,obj):
        return obj.comments.all().count()
    
    def get_comments(self,obj):
        qs=obj.comments.all()
        serializer_instance=CommentSerializer(qs,many=True)
        return serializer_instance.data
    
    def get_likes(self,obj):
        return obj.likes.all().count()

class CommentSerializer(serializers.ModelSerializer):
    issue=serializers.StringRelatedField(read_only=True)
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields="__all__"
        read_only_fields=["id","issue","user"]