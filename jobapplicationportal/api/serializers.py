from rest_framework import serializers
from .models import Job, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'applicant_name', 'email', 'applied_date', 'job']

    def validate(self, data):
        if Application.objects.filter(job=data['job'], email=data['email']).exists():
            raise serializers.ValidationError({"email": "This email has already applied for this job."})

        return data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.method == 'GET':
            data['job_title'] = instance.job.title
        return data
    
    
class UserApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    job_location = serializers.CharField(source='job.location', read_only=True)
    job_description = serializers.CharField(source='job.description', read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'applicant_name', 'email', 'applied_date', 'job', 'job_title', 'job_location', 'job_description']