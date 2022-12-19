from django.db import models
from django.utils.text import slugify
from django import forms
import re

# Create your models here.
class Guide(models.Model):
    name = models.CharField(help_text="Guide's Name - make unique", max_length=32, primary_key=True)
    title = models.CharField(help_text="Title at top of page", max_length=128)
    description = models.TextField(help_text="Description for top-level guide menu")
    about = models.TextField(help_text="Overal description of guide (in markdown) shows up on guide's frontpage")
    about_ending_media = models.TextField(blank=True, help_text="For media at the end of the about text, like a video. (in html)")
    tools_text = models.TextField(help_text="Text describing tools section (markdown)", blank=True)
    datasets_text = models.TextField(help_text="Text describing data section (markdown)" , blank=True)
    policies_text = models.TextField(help_text="Entire policies section (markdown)" , blank=True)
    display = models.BooleanField(help_text="Check to display on site")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super(Guide, self).save(*args, *kwargs)

class Tool(models.Model):
    title = models.CharField(max_length=64)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    description = models.TextField(help_text='Short description on front page')
    url = models.URLField()
    pic = models.ImageField(upload_to="toolpics")

    def __str__(self):
        return self.title


class DataSet(models.Model):
    # Front page stuff
    name = models.CharField(help_text="Unique name used in urls and backend", max_length=32, primary_key=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    title = models.CharField(help_text="Title that will display on site", max_length=64)
    description = models.TextField(help_text="Short description for front page")
    alert_text = models.TextField(blank=True)
    order = models.IntegerField()

    # Individual page stuff
    body_text = models.TextField("Body of text that will display on the DataSet's page (markdown)")
    things_to_know_block_text = models.TextField(help_text="Text that you can format yourself (markdown)", blank=True)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.name = slugify(self.name)
        super(DataSet, self).save(*args, *kwargs)


class PubliclyAvailableData(models.Model):
    text = models.CharField(max_length=200)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)


class NotPubliclyAvailableData(models.Model):
    text = models.CharField(max_length=200)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)


class WhereToFind(models.Model):
    text = models.TextField()
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)


class ThingsToKnow(models.Model):
    text = models.TextField()
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE)


