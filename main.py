from newsapi import NewsApiClient
from NewsAPIGetData.news_api_config import *
from NewsAPIGetData.fetch_news import *
import argparse
from helper_functions import Helper
from NewsAPIGetData.constants import *


def process_data(news_api, query, country, sources):
    fetch_data = FetchData(news_api, query, country)
    date_list = Helper.get_list_of_dates(num_days=32)
    if sources == 'ALL':
        sources_list = SOURCES_MAP[country]
        for source in sources_list:
            for date in date_list:
                all_articles = fetch_data.get_all_articles_last_month(page_no=1,
                                                                      page_size=100,
                                                                      from_param=date,
                                                                      to=date,
                                                                      sources=source,
                                                                      q_int_title=True)
                Helper.write_json(all_articles, query, country, source, date)
    else:
        for date in date_list:
            all_articles = fetch_data.get_all_articles_last_month(page_no=1,
                                                                  page_size=100,
                                                                  from_param=date,
                                                                  to=date,
                                                                  sources=sources,
                                                                  q_int_title=True)
            Helper.write_json(all_articles, query, country, sources, date)
    print('COMPLETED DUMPS!')


if __name__ == "__main__":
    news_api = NewsApiClient(api_key=API_KEY)

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", type=str, help="query term")
    parser.add_argument("-c", type=str, help="country code")
    parser.add_argument("-s", type=str, help=" 'ALL' or specific that matches NewsAPI Specs. Is OPTIONAL")

    args = parser.parse_args()

    query = args.q
    country = args.c
    sources = args.s

    process_data(news_api=news_api,
                 query=query,
                 country=country,
                 sources=sources)
