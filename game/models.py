from django.db import models

class TypeSpecialCard(models.Model):
    name = models.CharField(max_length=50)

class Card(models.Model):
    name = models.CharField(max_length=40)
    imageSource = models.CharField(max_length=255)
    text = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        abstract = True

class DefensiveCard(Card):
    value = models.FloatField()

class OffensiveCard(Card):
    value = models.FloatField()

class SpecialCard(Card):
    type = models.ForeignKey('TypeSpecialCard', on_delete=models.DO_NOTHING,)
    value = models.IntegerField()

class CharacterCard(Card):
    weakness = models.CharField(max_length=20)
    strength = models.CharField(max_length=20)
    maxAlcohol = models.FloatField()

class TypeStart(models.Model):
    name = models.CharField(max_length=30)


class TypeDeck(models.Model):
    name = models.CharField(max_length=30)


class TypeKickOff(models.Model):
    name = models.CharField(max_length=30)


class TypeEnding(models.Model):
    name = models.CharField(max_length=30)


class EndDeckEffect(models.Model):
    name = models.CharField(max_length=30)


class Parameters(models.Model):
    deckLimit = models.IntegerField()
    handSize = models.IntegerField()
    cardsPerTurn = models.IntegerField()
    cardsPerDraw = models.IntegerField()
    turnTimer = models.IntegerField()
    alcoholLimit = models.IntegerField()
    typeStart = models.ForeignKey('TypeStart', on_delete=models.DO_NOTHING,)
    typeDeck = models.ForeignKey('TypeDeck', on_delete=models.DO_NOTHING,)
    typeKickOff = models.ForeignKey('TypeKickOff', on_delete=models.DO_NOTHING,)
    endDeckEffect = models.ForeignKey('EndDeckEffect', on_delete=models.DO_NOTHING,)
    typeEnding = models.ForeignKey('TypeEnding', on_delete=models.DO_NOTHING,)