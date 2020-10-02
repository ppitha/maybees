from django.db import models
from datetime import date

from . import managers

# Create your models here.


class Apiary (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    primary_image = models.ImageField(upload_to='images/', blank=True, null=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)

    # Meta and String
    class Meta:
        verbose_name = "Apiary"
        verbose_name_plural = "Apiaries"

    def __str__(self):
        return "%s" % (self.name)

class Hive (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    primary_image = models.ImageField(upload_to='images/', blank=True, null=True)
    apiary_id = models.ForeignKey(
        Apiary, 
        on_delete=models.DO_NOTHING, 
        verbose_name='Apiary',
        related_name='hives')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    # these attributes could vary with time
    # brood_colony_size models.CharField(max_length=200) # deeps or mediums
    # bottom_board models.CharField(max_length=200) # screened or solid
    # TODO: create a configuration model (timestamped)?

    objects = managers.ProjectManager()
 
    # Meta and String
    class Meta:
        verbose_name = "Hive"
        verbose_name_plural = "Hives"

    def __str__(self):
        return "%s" % (self.name)

class Colony (models.Model):
    queen_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200)
    primary_image = models.ImageField(upload_to='images/', blank=True, null=True)
    source = models.CharField(max_length=100, blank=True)
    parent_id = models.ForeignKey("Colony", on_delete=models.DO_NOTHING, blank=True, null=True)

    # Meta and String
    class Meta:
        verbose_name = "Colony"
        verbose_name_plural = "Colonies"

    def __str__(self):
        return "%s" % (self.queen_name)

class Hive_Colony_Map (models.Model):
    hive_id = models.ForeignKey(Hive, on_delete=models.DO_NOTHING)
    colony_id = models.ForeignKey(Colony, on_delete=models.DO_NOTHING)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)
