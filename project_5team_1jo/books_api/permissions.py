from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		#정보를 읽는 경우(SAFE_METHODS: GET, HEAD, OPTIONS)  
		if request.method in permissions.SAFE_METHODS:
			return True
		
        #사용자가 일치하는지
		return obj.owner == request.user