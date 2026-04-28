from django.db import models
from causes.models import Cause
from accounts.models import CustomUser

class Donation(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True, blank=True, related_name='donations')
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cause:
            self.cause.raised_amount = sum(d.amount for d in self.cause.donations.all())
            self.cause.save()

    def __str__(self): return f"{self.donor_name} - UGX {self.amount}"
    class Meta: ordering = ['-created_at']

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self): return f"{self.name} - {self.subject}"
    class Meta: ordering = ['-created_at']
