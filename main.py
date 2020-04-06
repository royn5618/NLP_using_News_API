from newsapi import NewsApiClient
from NewsAPIGetData.news_api_config import *
from NewsAPIGetData.fetch_news import *
import math


def process_data(news_api, query, country, sources, daily = True):
    fetch_data = FetchData(news_api, query, country, sources)

    if daily:
        pass
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

    # TO DO : User Inputs
    query = 'foo'
    country = 'fooia'
    sources = 'foo-news'

    process_data(news_api, query, country, sources, daily=True)
