from django.shortcuts import render
from .models import Card
from .func_for_views import *


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


def multi_color_page(request):
    filtered_cards = sorting_by_color(color=None, colors_count=5)

    for card in filtered_cards:
        card.img = str(card.img).replace('large', 'border_crop')

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
        'title': "Multi-C Cards",
    }

    return render(request, 'magic/multi_color_page.html', context=context)


def color_page(request, color):
    filtered_cards = sorting_by_color(color=color.capitalize(), colors_count=1)

    for card in filtered_cards:
        card.img = str(card.img).replace('large', 'border_crop')

    title = f"{color.capitalize()} Cards"

    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
        'title': title,
        'color': color.capitalize(),
    }

    return render(request, 'magic/colors_list.html', context=context)
