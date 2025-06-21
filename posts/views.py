from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):  # ✅ This line enables GET requests
        return Response({"message": f"Hello, {request.user.username}!"})
