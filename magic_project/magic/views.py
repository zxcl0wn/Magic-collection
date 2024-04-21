import json

from django.shortcuts import render
from .models import Card


def card_string_to_list(string: str) -> list:
    return string.strip("[]").replace("'", "").split(", ")




def index(request):
    cards = Card.objects.all()
    for card in cards:
        card.img = str(card.img).replace('large', 'border_crop')
    context = {
        'cards': cards,
    }

    return render(request, 'magic/base.html', context=context)


# TODO вынести в отдельную функцию проверку на принадлежность цвету
def white_page(request):
    cards = Card.objects.all()
    filtered_cards = []
    for card in cards:
        colors_list = card_string_to_list(card.colors)
        if 'White' in colors_list and len(colors_list) == 1:
            filtered_cards.append(card)
            print(f'Карта белого цвета: {card.title} Цвета: {colors_list}')
    context = {
        'cards': filtered_cards
    }
    return render(request, 'magic/white_page.html', context=context)


def blue_page(request):
    cards = Card.objects.all()
    filtered_cards = []
    for card in cards:
        colors_list = card_string_to_list(card.colors)
        if 'Blue' in colors_list and len(colors_list) == 1:
            filtered_cards.append(card)
            print(f'Карта синего цвета: {card.title} Цвета: {colors_list}')
    context = {
        'cards': filtered_cards
    }
    return render(request, 'magic/blue_page.html', context=context)


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