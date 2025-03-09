from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer,UserApplicationSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-id') 
    serializer_class = JobSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-applied_date') 
    serializer_class = ApplicationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    

class UserApplicationsAPIView(APIView):
    permission_classes = [AllowAny]  
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description="User's email to filter applied jobs",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: UserApplicationSerializer(many=True),
            400: "Email parameter is required",
            404: "No applications found for this email",
        }
    )
 
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({"error": "Email parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not Application.objects.filter(email=email).exists():
            return Response({"error": "Email does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        applications = Application.objects.filter(email=email).select_related('job').order_by('-applied_date')

        if not applications.exists():
            return Response({"message": "No applications found for this email"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserApplicationSerializer(applications, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    