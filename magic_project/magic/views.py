import json

from django.shortcuts import render
from .models import Card


def card_string_to_list(string: str) -> list:
    return string.strip("[]").replace("'", "").split(", ")


# TODO создать ENUM для цветов и заменить прямое использование цвета

enum_all_colors = {
    "Белый": "White",
    "Синий": "Blue",
    "Черный": "Black",
    "Красный": "Red",
    "Зелёный": "Green",
    "Бесцветный": "Colorless",
}


def sorting_by_color(color: str, colors_count: int) -> list:
    cards = Card.objects.all()
    filtered_cards = []

    for card in cards:
        colors_list = card_string_to_list(card.colors)
        if color in colors_list:
            if len(colors_list) == colors_count:
                filtered_cards.append(card)
                print(f'Карта цвета {color}: {card.title} Цвета: {colors_list}')

    return filtered_cards


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
    filtered_cards = sorting_by_color('White', colors_count=1)

    context = {
        'cards': filtered_cards
    }
    return render(request, 'magic/white_page.html', context=context)


def blue_page(request):
    filtered_cards = sorting_by_color(color='Blue', colors_count=1)

    context = {
        'cards': filtered_cards
    }
    return render(request, 'magic/blue_page.html', context=context)


def black_page(request):
    filtered_cards = sorting_by_color(color='Black', colors_count=1)

    context = {
        'cards': filtered_cards
    }

    return render(request, 'magic/black_page.html', context=context)


def red_page(request):
    filtered_cards = sorting_by_color(color='Red', colors_count=1)

    context = {
        'cards': filtered_cards,
    }

    return render(request, 'magic/red_page.html', context=context)


def green_page(request):
    filtered_cards = sorting_by_color(color='Green', colors_count=1)

    context = {
        'cards': filtered_cards,
    }

    return render(request, 'magic/green_page.html', context=context)


def colorless_page(request):
    filtered_cards = sorting_by_color(color='Colorless', colors_count=1)

    context = {
        'cards': filtered_cards,
    }

    return render(request, 'magic/colorless_page.html', context=context)


def multi_color_page(request):
    # filtered_cards = sorting_by_color(color=, colors_count=5)
    pass