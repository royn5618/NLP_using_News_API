from newsapi import NewsApiClient
from DataProcessor.NewsAPIGetData.config_news_api import *
from DataProcessor.NewsAPIGetData.fetch_news import *
import argparse
from DataProcessor.helper_functions import Helper
from DataProcessor.NewsAPIGetData.constants import *


def process_data(query, country):
    Helper.read_json('Data/'+query)
    pass


def download_data(news_api, query, country, sources):
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
    parser.add_argument('-aim', type=str, choices=['download', 'process'])
    parser.add_argument("-q", type=str, help="query term")
    parser.add_argument("-c", type=str, help="country code only for aim - download | 'ALL' only for aim - process ")
    parser.add_argument("-s", type=str, help=" 'ALL' or specific that matches NewsAPI Specs. Is OPTIONAL")

    args = parser.parse_args()

    # Parse inputs
    aim = args.aim
    query = args.q
    country = args.c
    sources = args.s

    if aim == 'download':
        if query and country and sources:
            download_data(news_api=news_api, query=query, country=country, sources=sources)
        else:
            raise ValueError("Re-validate input arguments!")

    elif aim == 'process':
        if query:
            '''
            LOGIC:
            Should process 
            * multiple queries
            * Processes all countries that were queried
            '''
            if ',' in query:
                q_input_list = query.split(',')
            else:
                q_input_list = [query]
            try:
                if Helper.verify_q_terms(q_input_list):
                    process_data(query=query)
            except ValueError as err:
                print(err)
