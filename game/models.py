from django.db import models

class TypeSpecialCard(models.Model):
    name = models.CharField(max_length=50)

class Card(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    imageSource = models.CharField(max_length=255)
    text = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        abstract = True

class DefensiveCard(Card):
#    id = models.OneToOneField(Card)
    value = models.FloatField()

class OffensiveCard(Card):
    #id = models.OneToOneField(Card)
    value = models.FloatField()

class SpecialCard(Card):
 #   id = models.OneToOneField(Card)
    type = models.ForeignKey('TypeSpecialCard', on_delete=models.DO_NOTHING,)
    value = models.IntegerField()

class CharacterCard(Card):
   # id = models.OneToOneField(Card)
    weakness = models.CharField(max_length=20)
    strength = models.CharField(max_length=20)
    maxAlcohol = models.FloatField()

