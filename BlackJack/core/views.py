from django.shortcuts import render
from .models import Deck, Hand

def start_game(request):
    # Create a Hand instance and add cards to it
    hand = Hand.objects.create()

    for i in range(2):
        drawn_card = Deck.draw_card()
        hand.cards.add(drawn_card)

    context = {
        'hand': hand,
    }

    return render(request, 'index.html', context)
