from django.db import models


class GenderChoice(models.TextChoices):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'


class GroupChoices(models.TextChoices):
    work = 'Work'
    study = 'Study'
    environment = 'environment'
    family = 'Family'


class User(models.Model):
    birthdate = models.DateTimeField(null=True)
    name = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, null=True)


class Item(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=255, null=False)
    group = models.CharField(max_length=255, null=False, choices=GroupChoices.choices)
    user_item = models.ManyToOneRel(to=User, field=User, field_name='user_item')
