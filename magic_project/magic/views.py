from django.shortcuts import render
from .models import Card


def index(request):
    cards = Card.objects.all()
    print(cards)
    context = {
        'cards': cards,
    }
    print(context)
    return render(request, 'magic/index.html', context=context)

