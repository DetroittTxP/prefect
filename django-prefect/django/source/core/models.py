from django.db import models

# Create your models here.


class UserAsset(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    asset = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=50)
    asset_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.asset}"
