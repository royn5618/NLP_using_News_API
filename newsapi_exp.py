# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:25:44 2020

@author: Owner
"""

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b9c44be5bd4e476f87a5d8781ae57d09')
countries_mapper = {'India':'in', 
                    'Ireland':'ie',
                    'UK':'gb', 
                    'USA':'us'}

source_mapper = {'India': 'the-times-of-india',
                 'Ireland' : 'the-irish-times'}


def get_top_headline_by_country(country,page_no=1, page_size=100):
    return newsapi.get_top_headlines(country=country,
                                     page=page_no,
                                     page_size=page_size)


def get_all_articles_last_month(country, query, source, page_no):
    return newsapi.get_everything(q=query,
                                  sources=source,
                                  language='en',
                                  page=page_no,
                                  page_size=100)
    
import json

with open('data.txt', 'w') as outfile:
    json.dump(get_top_headline_by_country('in'), outfile)
