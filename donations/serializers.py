from rest_framework import serializers
from .models import Donation, ContactSubmission

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id','cause','donor_name','donor_email','amount','message','is_anonymous','created_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['id','name','email','subject','message','created_at']
