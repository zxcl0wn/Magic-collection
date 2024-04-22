import json

from django.shortcuts import render
from .models import Card


def card_string_to_list(string: str) -> list:
    return string.strip("[]").replace("'", "").split(", ")


enum_all_tabs = {
    'White': "px-4 py-2 rounded-md hover:bg-white hover:text-gray-900",
    'Blue': "px-4 py-2 rounded-md hover:bg-blue-500 hover:text-white",
    'Black': "px-4 py-2 rounded-md hover:bg-black hover:text-white",
    'Red': "px-4 py-2 rounded-md hover:bg-red-500 hover:text-white",
    'Green': "px-4 py-2 rounded-md hover:bg-green-500 hover:text-white",
    'Colorless': "px-4 py-2 rounded-md hover:bg-gray-500 hover:text-white",
    'Multi-C': "px-4 py-2 rounded-md hover:bg-yellow-500 hover:text-white",
    'Collection': "px-4 py-2 rounded-md hover:bg-purple-500 hover:text-white",
}


def sorting_by_color(color=None, colors_count=None) -> list:
    cards = Card.objects.all()
    filtered_cards = []

    if colors_count == 1:
        for card in cards:
            colors_list = card_string_to_list(card.colors)
            if color in colors_list:
                if len(colors_list) == colors_count:
                    filtered_cards.append(card)
                    print(f'Карта цвета {color}: {card.title} Цвета: {colors_list}')

    elif colors_count == 5:
        for card in cards:
            colors_list = card_string_to_list(card.colors)
            if len(colors_list) > 1:
                filtered_cards.append(card)
                print(f'Карта цвета {color}: {card.title} Цвета: {colors_list}')

    return filtered_cards


def index(request):
    cards = Card.objects.all()
    for card in cards:
        card.img = str(card.img).replace('large', 'border_crop')
    context = {
        'cards': cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/base.html', context=context)


def white_page(request):
    filtered_cards = sorting_by_color(color='White', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }
    return render(request, 'magic/white_page.html', context=context)


def blue_page(request):
    filtered_cards = sorting_by_color(color='Blue', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }
    return render(request, 'magic/blue_page.html', context=context)


def black_page(request):
    filtered_cards = sorting_by_color(color='Black', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/black_page.html', context=context)


def red_page(request):
    filtered_cards = sorting_by_color(color='Red', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/red_page.html', context=context)


def green_page(request):
    filtered_cards = sorting_by_color(color='Green', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/green_page.html', context=context)


def colorless_page(request):
    filtered_cards = sorting_by_color(color='Colorless', colors_count=1)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/colorless_page.html', context=context)


def multi_color_page(request):
    filtered_cards = sorting_by_color(color=None, colors_count=5)

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
    }

    return render(request, 'magic/multi_color_page.html', context=context)
