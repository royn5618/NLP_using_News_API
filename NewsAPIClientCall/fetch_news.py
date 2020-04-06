from NewsAPIClientCall import constants


class FetchData:
    def __init__(self, news_api):
        """
        :param news_api: news api client object
        """""
        self.news_api = news_api

    def get_top_headline_by_country(self, country, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param country: 2-letter ISO 3166-1 code of the country
                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        return self.news_api.get_top_headlines(country=country,
                                               page=page_no,
                                               page_size=page_size)

    def get_all_articles_last_month(self, query, sources, page_no=1, page_size=100):
        """
                To fetch the top headlines in news.

                :param query: query term / keyword
                :param sources: comma-separated string of sources
                :param page_size: number of results to return per page request.
                In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:
        """
        return self.news_api.get_everything(q=query,
                                            sources=sources,
                                            page=page_no,
                                            page_size=page_size)

    def get_top_headline_by_source(self, sources, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param sources: source id in NewsAPI
                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        return self.news_api.get_top_headlines(source=sources,
                                               page=page_no,
                                               page_size=page_size)