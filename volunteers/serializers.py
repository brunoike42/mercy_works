from rest_framework import serializers
from .models import VolunteerOpportunity, VolunteerApplication

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerOpportunity
        fields = ['id','title','description','requirements','location','is_active','created_at']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerApplication
        fields = ['id','opportunity','name','email','phone','message','status','created_at']
        read_only_fields = ['status']
