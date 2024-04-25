from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import Card, Set
from .func_for_views import *
from constants import *
import re


enum_all_tabs = {
    'White': "px-4 py-2 rounded-md hover:bg-white hover:text-gray-900",
    'Blue': "px-4 py-2 rounded-md hover:bg-blue-500 hover:text-white",
    'Black': "px-4 py-2 rounded-md hover:bg-black hover:text-white",
    'Red': "px-4 py-2 rounded-md hover:bg-red-500 hover:text-white",
    'Green': "px-4 py-2 rounded-md hover:bg-green-500 hover:text-white",
    'Colorless': "px-4 py-2 rounded-md hover:bg-gray-500 hover:text-white",
    'Multicolor': "px-4 py-2 rounded-md hover:bg-yellow-500 hover:text-white",
    'Collection': "px-4 py-2 rounded-md hover:bg-purple-500 hover:text-white",
}

cards_icons = CARDS_ICONS


def color_page(request, color):
    if color != "Multicolor":
        filtered_cards = sorting_by_color(color=color.capitalize(), colors_count=1)
    else:
        filtered_cards = sorting_by_color(color=None, colors_count=5)

    if len(filtered_cards) == 0:
        raise Http404()

    print(f'\n\nТеги цвета {color}')
    regexp = r"({.+?})"

    for card in filtered_cards:
        card.img = str(card.img).replace('large', 'border_crop')

        print(f'Описание карты {card.title}:')
        for tag in card.tags:
            print(f'{tag}: {card.tags[tag]}')
        print(f'\n\n')

        if card.mana_cost is not None:
            card.mana_cost = re.sub(regexp, lambda match: f"<img class='w-5 inline' src='{cards_icons.get(match.group(1), '')}' />", card.mana_cost)

        if card.oracle_text is not None:
            card.oracle_text = re.sub(regexp, lambda match: f"<img class='pb-[4px] w-4 inline' src='{cards_icons.get(match.group(1), '')}' />", card.oracle_text)

    title = f"{color.capitalize()} Cards"


    context = {
        'cards': filtered_cards,
        'tabs': enum_all_tabs,
        'title': title,
        'color': color.capitalize(),

    }
    return render(request, 'magic/colors_list.html', context=context)


# def pageNotFound(request, exception):
#     return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def delete_card(card_id):
    try:
        card = Card.objects.get(id=card_id)
        card.delete()
        print(f'Карта {card.title} удалена из БД')
    except Exception as e:
        print(f'Карты по id {card_id} не существует')
        return None


def update_card(card_id, new_title=None, new_oracle_text=None, new_flavor_text=None, new_mana_cost=None, new_colors=None, new_tags=None, new_img=None):
    card = Card.objects.get(id=card_id)

    if new_title is not None:
        card.title = new_title
    if new_oracle_text is not None:
        card.oracle_text = new_oracle_text
    if new_flavor_text is not None:
        card.flavor_text = new_flavor_text
    if new_mana_cost is not None:
        card.mana_cost = new_mana_cost
    if new_colors is not None:
        card.colors = new_colors
    if new_tags is not None:
        card.tags = new_tags
    if card.img is not None:
        card.img = new_img

    print(f'Информация о карте {card.title} обновлена')
    card.save()


def delete_set(set_id):
    try:
        set_del = Set.objects.get(id=set_id)
        set_del.delete()
        print(f'Сет {set_del.name} удален из БД')
    except Exception as e:
        print(f'Сета по id {set_id} не существует')
        return None


def update_set(set_id, new_name=None):
    set = Set.objects.get(id=set_id)

    if new_name is not None:
        set.name = new_name

    print(f'Информация о сете {set.name} обновлена')
    set.save()