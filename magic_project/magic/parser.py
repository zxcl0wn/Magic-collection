import time
import socks
import socket
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import json
import helium
from magic.models import *


class Parser:
    def __init__(self, url):
        self.url = url

    def get_tags(self, url):
        tags_dict = {}
        helium.go_to(url)
        helium.wait_until(lambda: helium.S('.taggings').web_element.is_displayed())
        all_tags = helium.find_all(helium.S('.taggings'))

        artwork_tags = list(all_tags[0].web_element.text.split('\n'))
        tags_dict['Artwork'] = artwork_tags

        elements_card_tags = all_tags[1].web_element
        card_tags_html = elements_card_tags.get_attribute('innerHTML')
        soup = BeautifulSoup(card_tags_html, 'html.parser')
        desired_elements = soup.find_all(class_='tag-row-flex')

        card_tags = []
        for element in desired_elements:
            card_tags.append(element.text)
        tags_dict['Card'] = card_tags

        return tags_dict

    def determination_color(self, bracket_color: str, oracle_text: str) -> list:
        card_color = set()
        if bracket_color is None:
            bracket_color = ''

        if oracle_text is not None:
            bracket_color += self.colors_in_oracle(oracle_text)
        delete_char = str.maketrans("", "", '0123456789{}')
        bracket_color = bracket_color.translate(delete_char)
        all_colors = {
            'G': "Green",
            'W': "White",
            'R': "Red",
            'B': "Black",
            'U': "Blue",
            'C': "Colorless"
        }

        if bracket_color:
            for i in bracket_color:
                if i in all_colors:
                    card_color.add(all_colors[i])
        else:
            card_color.add('Colorless')

        if "Colorless" in card_color and len(card_color) > 1:
            card_color.remove('Colorless')

        return sorted(list(card_color))

    def colors_in_oracle(self, oracle_text: str) -> str:
        colors_list = ['{W}', '{G}', '{B}', '{R}', '{C}', '{U}']
        oracle_colors = ''
        for i in colors_list:
            if i in oracle_text:
                oracle_colors += i

        return oracle_colors

    def parser(self, url):
        card = Card()
        response = requests.get(url=url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        if len(soup.find_all(class_="card-text-title")) > 1:
            print(f'У карты больше одного названия!!!')
            return None

        card.title = soup.find(class_='card-text-card-name').text.strip()
        print(f'Карта: {card.title}')
        # card_dict['card_type'] = soup.find(class_='card-text-type-line').text.strip().split(' — ')[0]  # TODO
        card.img = soup.find(class_='card-image-front').img['src']

        if soup.find(class_='card-text-oracle'):
            card.oracle_text = soup.find(class_='card-text-oracle').text.strip().replace('\n', ' ')
        else:
            card.oracle_text = None

        if soup.find(class_='card-text-flavor'):
            card.flavor_text = soup.find(class_='card-text-flavor').text.strip()
        else:
            card.flavor_text = None

        if soup.find(class_='card-text-mana-cost'):
            card.mana_cost = soup.find(class_='card-text-mana-cost').text.strip()
        else:
            card.mana_cost = None

        card.colors = self.determination_color(card.mana_cost, card.oracle_text)

        card_set_name = soup.find(class_='prints-current-set-name').text.strip()
        # Проверяем существует ли такой набор, если нет - создаем новый
        card_set, _ = Set.objects.get_or_create(name=card_set_name)
        card.set = card_set

        cm_link = soup.find('a', class_='button-n', title='Tag card', rel='nofollow').get('href')
        print(f'cm_link: {cm_link}')
        card.tags = self.get_tags(cm_link)

        card.save()
        print(f'Карта сохранена в базу данных')
        return card
