import json

from django.shortcuts import render
from .models import Card


def index(request):
    cards = Card.objects.all()
    for card in cards:
        card.img = str(card.img).replace('large', 'border_crop')
    context = {
        'cards': cards,
    }

    return render(request, 'magic/base.html', context=context)


def white_page(request):
    cards = Card.objects.all()
    filtered_cards = []
    for card in cards:
        colors_list = card.colors.strip("[]").replace("'", "").split(", ")
        if 'White' in colors_list and len(colors_list) == 1:
            filtered_cards.append(card)
            print(f'Карта белого цвета: {card.title} Цвета: {colors_list}')
    context = {
        'cards': filtered_cards
    }
    return render(request, 'magic/white_page.html', context=context)


def blue_page(request):
    pass


def black_page(request):
    pass


def red_page(request):
    pass


def green_page(request):
    pass


def colorless_page(request):
    pass


def multi_color_page(request):
    pass