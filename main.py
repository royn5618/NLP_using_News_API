from newsapi import NewsApiClient
from NewsAPIGetData.news_api_config import *
from NewsAPIGetData.fetch_news import *
import math
import argparse
from helper_functions import Helper


def process_data(news_api, query, country, sources=None, daily=True):
    fetch_data = FetchData(news_api, query, country, sources)

    if daily:
        all_articles = fetch_data.get_top_headline_by_country()
        Helper.write_json(all_articles, query, country, sources)
    else:
        # Monthly
        '''
        Monthly I want  to get Indian and Irish News on Coronavirus.
        For this I will use fetch everything.
        Storage: Folder "Month_<no>" -> country_name -> json#.json
        Each json contains <= 100 objects
        '''
        no_of_articles = None
        all_articles = fetch_data.get_all_articles_last_month(page_no=1, page_size=100)
        no_of_articles = all_articles['totalResults']
        page_requests = math.ceil(no_of_articles/100)

        if page_requests == 1:
            # TO DO: Store the data in apt folder
            pass
        else:
            # ITERATE and then Store
            for i in range(1, page_requests + 1):
                all_articles = fetch_data.get_all_articles_last_month(page_no=1, page_size=100)


if __name__ == "__main__":
    news_api = NewsApiClient(api_key=API_KEY)

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, help="query term")
    parser.add_argument("-c", type=str, help="country")
    parser.add_argument("-d", type=bool, help="Daily? True or False")

    args = parser.parse_args()

    query = args.q
    country = args.c
    daily = args.d
    # import pdb
    # pdb.set_trace()
    process_data(news_api, query, country)
