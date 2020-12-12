from django.db import models

from accounts.models import User


class Folder(models.Model):
    name = models.CharField(max_length=250, default='Incomplete')
    serie = models.CharField(max_length=10, default='Incomplete')
    from_date = models.DateField(null=True, blank=True, default=None)
    to_date = models.DateField(null=True, blank=True, default=None)
    from_guide = models.CharField(max_length=15, blank=True, default=None)
    to_guide = models.CharField(max_length=15, blank=True, default=None)
    code = models.CharField(max_length=10, default='Incomplete')
    is_full = models.BooleanField(default=False)
    color = models.CharField(max_length=10, default='white')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Missing(models.Model):
    guide = models.CharField(max_length=25)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.guide
