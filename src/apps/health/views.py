from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .services import health_service


class HealthView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        result = health_service.check()
        h = result.data
        code = (
            status.HTTP_200_OK
            if h.status == "healthy"
            else status.HTTP_503_SERVICE_UNAVAILABLE
        )
        return Response(h.to_dict(), status=code)


class LiveView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"status": "alive"})


class ReadyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        result = health_service.check()
        if result.data.status == "healthy":
            return Response({"status": "ready"})
        return Response(
            {"status": "not_ready"}, status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
