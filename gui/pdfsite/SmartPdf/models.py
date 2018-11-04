from django.db import models

class File(models.Model):

    name = models.CharField(max_length=255)
    pages = models.CharField(max_length=15)
    check = models.BooleanField(default = False)
    watermark = models.CharField(max_length=255, default = "")

    class Meta:
        db_table = 'file'

    def __str__(self):
        return self.name