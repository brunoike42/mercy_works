from django.db import models

class Cause(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='causes/', blank=True, null=True)
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def progress_percent(self):
        if self.goal_amount > 0:
            return min(int((self.raised_amount / self.goal_amount) * 100), 100)
        return 0

    def __str__(self): return self.title
    class Meta: ordering = ['-is_featured', '-created_at']
