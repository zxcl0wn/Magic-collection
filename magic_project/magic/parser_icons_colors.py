from bs4 import BeautifulSoup
import requests
import json
import helium
from magic.models import *


class ParserIcons:
    def __init__(self, url):
        self.url = url

    def parser_icons(self, url):
        response = requests.get(url=url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

