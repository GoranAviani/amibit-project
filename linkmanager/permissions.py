from rest_framework.permissions import BasePermission


#class IsOwnerOrReadOnly(BasePermission):
#    message='If you want to update you must be the over of this project'
#    def has_object_permission(self, request,view,obj):
#        return obj.link_user == request.user
