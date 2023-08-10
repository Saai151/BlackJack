from django.db import models

class Deck(models.Model):
    RANK_CHOICES = [
        ('A', 'ace'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('T', '10'),
        ('J', '11'),
        ('Q', '12'),
        ('K', '13'),
    ]

    SUIT_CHOICES = [
        ('H', 'Hearts'),
        ('C', 'Clubs'),
        ('S', 'Spades'),
        ('D', 'Diamonds'),
    ]

    rank = models.CharField(max_length=1, choices=RANK_CHOICES)
    suit = models.CharField(max_length=1, choices=SUIT_CHOICES)

    def __str__(self):
        return f"{self.get_rank_display()} of {self.get_suit_display()}"

    @staticmethod
    def draw_card():
        # Draw a random card from the deck
        return Deck.objects.order_by('?').first()

class Hand(models.Model):
    cards = models.ManyToManyField(Deck)

