from django.test import TestCase
from constants import *
from magic.parser import *
from magic.func_for_views import *
from magic.models import *


class ParserTest(TestCase):
    helium.start_chrome(headless=True)

    def test_get_tags(self):
        url = 'https://tagger.scryfall.com/card/mkc/202'
        parser = Parser(url)
        tags_dict = parser.get_tags(url)

        self.assertIn('Artwork', tags_dict)
        self.assertIn('Card', tags_dict)


    def test_colors_in_oracle(self):
        parser = Parser('')

        all_colors = {
            '{G}': '{G}',
            '{W}': '{W}',
            '{R}': '{R}',
            '{U}': '{U}',
            '{B}': '{B}',
            '{C}': '{C}',
            '{G}{W}': '{G}{W}',
            '{R}{G}': '{R}{G}',
            '{B}{U}': '{B}{U}',
            '{R}{W}': '{R}{W}',
            '{U}{B}': '{U}{B}',
            '{W}{U}': '{W}{U}',
            '{W}{U}{B}': '{W}{U}{B}',
            '{U}{B}{R}': '{U}{B}{R}',
            '{B}{R}{G}': '{B}{R}{G}',
            '{R}{G}{W}': '{R}{G}{W}',
            '{B}{B}{R}': '{B}{R}',
            '{R}{W}{G}{B}': '{R}{W}{G}{B}',
            '{W}{G}{U}{R}': '{W}{G}{U}{R}',
            '{G}{U}{B}{W}': '{G}{U}{B}{W}',
            '{W}{U}{B}{R}{G}': '{W}{U}{B}{R}{G}'
        }

        for key, value in all_colors.items():
            result = parser.colors_in_oracle(key).replace('{', '').replace('}', '')
            expected = value.replace('{', '').replace('}', '')
            self.assertEqual(sorted(result), sorted(expected))

    def test_determination_color(self):
        parser = Parser('')

        bracket_color = '{W}{U}{B}'
        oracle_text = '{W}{B}{R}'

        self.assertEqual(parser.determination_color(bracket_color, oracle_text), sorted(['White', 'Blue', 'Black', 'Red']))

    def test_parser(self):
        url = URL_CHULANE
        parser = Parser(url)

        card = parser.parser(url)

        self.assertEqual(card.title, 'Chulane, Teller of Tales')
        self.assertEqual(card.oracle_text, 'Vigilance\nWhenever you cast a creature spell, draw a card, then you may put a land card from your hand onto the battlefield.\n{3}, {T}: Return target creature you control to its owner’s hand.')
        self.assertEqual(card.flavor_text, None)
        self.assertEqual(card.mana_cost, '{2}{G}{W}{U}')
        self.assertEqual(card.img, 'https://cards.scryfall.io/large/front/d/1/d1499a4b-1af1-4913-8e26-57d0707264db.jpg?1706240978')

    def test_card_string_to_list(self):
        colors_string = "['White', 'Blue', 'Black', 'Red', 'Green']"

        self.assertEqual(card_string_to_list(colors_string), ['White', 'Blue', 'Black', 'Red', 'Green'])

    def setUp(self):
        set1 = Set(name='Set1')
        set1.save()

        self.card1 = Card.objects.create(title='Card1', colors=['White'], set_id=1)
        self.card2 = Card.objects.create(title='Card2', colors=['Blue'], set_id=1)
        self.card3 = Card.objects.create(title='Card3', colors=['Green'], set_id=1)
        self.card4 = Card.objects.create(title='Card4', colors=['Red'], set_id=1)
        self.card5 = Card.objects.create(title='Card5', colors=['Black', 'Red', 'Green'], set_id=1)

    def test_sorting_by_single_color(self):
        # Фильтруем карты по одному цвету
        filtered_cards = sorting_by_color(color='White', colors_count=1)

        self.assertIn(self.card1, filtered_cards)
        self.assertNotIn(self.card2, filtered_cards)
        self.assertNotIn(self.card3, filtered_cards)
        self.assertNotIn(self.card4, filtered_cards)
        self.assertNotIn(self.card5, filtered_cards)

    def test_sorting_by_multiple_colors(self):

        filtered_cards = sorting_by_color(color=None, colors_count=5)

        self.assertNotIn(self.card1, filtered_cards)
        self.assertNotIn(self.card2, filtered_cards)
        self.assertNotIn(self.card3, filtered_cards)
        self.assertNotIn(self.card4, filtered_cards)
        self.assertIn(self.card5, filtered_cards)