from rest_framework import serializers
from .models import Cause

class CauseSerializer(serializers.ModelSerializer):
    progress_percent = serializers.IntegerField(read_only=True)
    class Meta:
        model = Cause
        fields = ['id','title','description','image','goal_amount','raised_amount','progress_percent','is_active','is_featured','created_at']
