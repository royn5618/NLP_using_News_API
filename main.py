from newsapi import NewsApiClient
from NewsAPIGetData.news_api_config import *
from NewsAPIGetData.fetch_news import *
import math
import argparse
from helper_functions import Helper


def process_data(news_api, query, country, daily, sources=None):
    fetch_data = FetchData(news_api, query, country, sources)
    if daily:
        all_articles = fetch_data.get_top_headline_by_country()
        Helper.write_json(all_articles, query, country)
    else:
        # Monthly
        # ITERATE and then Store
        date_list = Helper.get_list_of_dates(num_days=32)
        for date in date_list:
            all_articles = fetch_data.get_all_articles_last_month(page_no=1,
                                                                  page_size=100,
                                                                  from_param=date,
                                                                  to=date,
                                                                  q_int_title=True)
            Helper.write_json(all_articles, query, country, date)
        print('COMPLETED DUMPS!')


if __name__ == "__main__":
    news_api = NewsApiClient(api_key=API_KEY)

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, help="query term")
    parser.add_argument("-c", type=str, help="country")
    parser.add_argument("-d", type=bool, default=False, help="Daily? True or False")

    args = parser.parse_args()

    query = args.q
    country = args.c
    daily = args.d

    process_data(news_api, query, country, daily)
