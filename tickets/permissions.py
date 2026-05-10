from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        #obj of expense takes the id
        return request.user==obj.reported_by