from django.db import models
from django import forms

class Bus(models.Model):
    bno = models.IntegerField()
    broute = models.CharField(max_length=300)
    btime = models.TextField()
    bcon = models.TextField()
    bdri = models.TextField()

class Busform(forms.ModelForm):
    class Meta:
        model = Bus
        exclude = ()


