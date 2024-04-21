import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magic_project.magic_project.settings')
django.setup()

import helium
from magic_project.constants import *
from parser import Parser


def main():
    url = URL_RANDOM
    parser1 = Parser(url)
    helium.start_firefox()
    count = 0
    for i in range(100):
        count += 1
        one_card = parser1.parser(url)
        print(f'Карта {count + 1}: \t{one_card}\n\n')


if __name__ == '__main__':
    main()
