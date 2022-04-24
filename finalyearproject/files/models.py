from django.db import models

# Create your models here.


class Scan(models.Model):
    name = models.CharField(max_length= 255, blank=False, null=False)
    image = models.ImageField(upload_to='scans/', null=True, max_length=255)

    def __repr__(self):
        return 'Scan(%s, %s)' % (self.name, self.image)

    def __str__ (self):
        return self.name