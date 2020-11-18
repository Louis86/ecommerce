from django.db import models
#data object
# Create your models here.

class Pages(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)#link limited to 12
    update_date = models.DateTimeField('Last Update')
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title
