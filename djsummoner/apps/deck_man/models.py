from django.db import models


class Ability(models.Model):
    ability_title = models.CharField(max_length=50)
    ability_description = models.TextField()

    class Meta(object):
        abstract = True


class BasicUnit(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()
    ranged = models.BooleanField()

    class Meta(object):
        abstract = True


class Unit(BasicUnit, Ability):
    cost = models.IntegerField()
    champion = models.BooleanField(default=False)


class Summoner(BasicUnit, Ability):
    pass


class Event(Ability):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(blank=True)


class Deck(models.Model):
    title = models.CharField(max_length=50)
    race = models.CharField(max_length=20)
    units = models.ManyToManyField('Unit')
    events = models.ManyToManyField('Event')
    summoner = models.ForeignKey('Summoner')
