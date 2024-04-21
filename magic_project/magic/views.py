from django.shortcuts import render
from .models import Card


def index(request):
    cards = Card.objects.all()
    for card in cards:
        card.img = str(card.img).replace('large', 'border_crop')
    context = {
        'cards': cards,
    }
    return render(request, 'magic/index.html', context=context)

