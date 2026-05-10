from rest_framework import serializers
from tickets.models import User,RoadIssue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password","phone"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class IssueSerializer(serializers.ModelSerializer):
    reported_by=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=RoadIssue
        fields="__all__"
        read_only_fields=["id","reported_by","created_at","updated_at"]