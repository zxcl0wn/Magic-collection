import time
import socks
import socket
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import json
import helium


class Parser:
    def __init__(self, url):
        self.url = url

