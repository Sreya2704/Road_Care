from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        #obj of expense takes the id
        return request.user==obj.reported_by
    
class IsCommentOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user