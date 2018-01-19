#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:18:58 2017

@author: quang
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://projects.fivethirtyeight.com/soccer-predictions/premier-league/")

soup = BeautifulSoup(response.text, "html.parser")

intro = soup.select('div.games-container.completed div.match-container.initial-view')[0]


