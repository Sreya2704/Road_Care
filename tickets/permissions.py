from rest_framework.permissions import BasePermission
from tickets.models import Comment,RoadIssue

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj,Comment):
            return request.user == obj.user
        
        if isinstance(obj,RoadIssue):
            return request.user == obj.reported_by
    






    
# class IsCommentOwner(BasePermission):

#     def has_object_permission(self, request, view, obj):
#         return request.user == obj.user