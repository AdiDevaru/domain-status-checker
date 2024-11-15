from django.db import models

# Create your models here.
class InitialUrls(models.Model):
    scan_id = models.IntegerField()
    url = models.URLField(max_length=200)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.url

class FinalUrls(models.Model):
    scan_id = models.IntegerField()
    url = models.URLField(max_length=200)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.url