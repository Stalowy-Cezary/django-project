from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Raid(models.Model):

    class Meta:
        pass
    name = models.CharField(max_length=50)



    def get_absolute_url(self):
        return reverse('raid-detail', args=[slugify(str(self.name))])

    def __str__(self):
        return self.name

class Boss(models.Model):

    class Meta:
        verbose_name_plural = 'Bosses'
        ordering = ['id']

    name = models.CharField(max_length=100)
    raid_wing = models.ForeignKey(Raid, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('wings', args=[str(self.name)])

    def __str__(self):
        return self.name