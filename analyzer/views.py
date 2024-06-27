from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import GenericAPIView

from .utils import analyze_urine_strip
from .serializers import ImageUploadSerializer

def index(request): 
    return render(request, 'index.html')

class ImageUploadView(GenericAPIView):
    """
    API Endpoint to get urine analysis test
    """
    serializer_class = ImageUploadSerializer
    parser_classes = [MultiPartParser]
    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        image = serializer.validated_data["image"]
        colors = analyze_urine_strip(image)
        return Response(colors, status=status.HTTP_200_OK)
