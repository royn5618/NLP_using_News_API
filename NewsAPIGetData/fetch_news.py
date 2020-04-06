class FetchData:
    def __init__(self, news_api, query, country, sources):
        """

        :param news_api: NewsAPI object
        :param query: query term
        :param country: country code
        :param sources: comma separated source ids from NewsAPI
        """
        self.news_api = news_api
        self.country = country
        self.sources = sources
        self.query = query

    def get_top_headline_by_country(self, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        return self.news_api.get_top_headlines(country=self.country,
                                               page=page_no,
                                               page_size=page_size)

    def get_all_articles_last_month(self, page_no=1, page_size=100):
        """
                To fetch the top headlines in news.

                :param page_size: number of results to return per page request.
                In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:
        """
        return self.news_api.get_everything(q=self.query,
                                            sources=self.sources,
                                            page=page_no,
                                            page_size=page_size)

    def get_top_headline_by_source(self, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        return self.news_api.get_top_headlines(source=self.sources,
                                               page=page_no,
                                               page_size=page_size)