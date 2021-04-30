from django.db import models

# Create your models here.
class Presence(models.Model):

    CLASSROOM_CHOICES = [
        ('X CG 1', 'X CG 1'),
        ('X PS 1', 'X PS 1'),
        ('X MM 1', 'X MM 1'),
        ('X TKJ 1', 'X TKJ 1'),
        ('X RPL 1', 'X RPL 1'),
        ('XI CG 1', 'XI CG 1'),
        ('XI PS 1', 'XI PS 1'),
        ('XI MM 1', 'XI MM 1'),
        ('XI TKJ 1', 'XI TKJ 1'),
        ('XI RPL 1', 'XI RPL 1'),
        ('XII CG 1', 'XII CG 1'),
        ('XII PS 1', 'XII PS 1'),
        ('XII MM 1', 'XII MM 1'),
        ('XII TKJ 1', 'XII TKJ 1'),
        ('XII RPL 1', 'XII RPL 1')
    ]

    name = models.CharField('name', max_length=50)
    classroom = models.CharField('classroom', choices=CLASSROOM_CHOICES, max_length=40)
    summary = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    CLASSROOM_CHOICES = [
        ('X CG 1', 'X CG 1'),
        ('X PS 1', 'X PS 1'),
        ('X MM 1', 'X MM 1'),
        ('X TKJ 1', 'X TKJ 1'),
        ('X RPL 1', 'X RPL 1'),
        ('XI CG 1', 'XI CG 1'),
        ('XI PS 1', 'XI PS 1'),
        ('XI MM 1', 'XI MM 1'),
        ('XI TKJ 1', 'XI TKJ 1'),
        ('XI RPL 1', 'XI RPL 1'),
        ('XII CG 1', 'XII CG 1'),
        ('XII PS 1', 'XII PS 1'),
        ('XII MM 1', 'XII MM 1'),
        ('XII TKJ 1', 'XII TKJ 1'),
        ('XII RPL 1', 'XII RPL 1')
    ]

    name = models.CharField('name', max_length=50)
    classroom = models.CharField('classroom', choices=CLASSROOM_CHOICES, max_length=40)
    question1 = models.CharField('1', max_length=5000)
    question2 = models.CharField('2', max_length=5000)
    question3 = models.CharField('3', max_length=5000)
    question4 = models.CharField('4', max_length=5000)
    question5 = models.CharField('5', max_length=5000)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
