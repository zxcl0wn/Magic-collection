from magic.models import Card


def card_string_to_list(string: str) -> list:
    return string.strip("[]").replace("'", "").split(", ")


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