class FetchData:

    def __init__(self, news_api, query, country):
        """

        :param news_api: NewsAPI object
        :param query: query term
        :param country: country code
        """
        self.news_api = news_api
        self.country = country
        self.query = query

    def get_top_headline_by_country(self, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        try:
            return self.news_api.get_top_headlines(country=self.country,
                                                   page=page_no,
                                                   page_size=page_size)
        except Exception as e:
            print(e)
        return None

    def get_all_articles_last_month(self, from_param, to, sources, page_no=1, page_size=100, q_int_title=False):
        """
                To fetch the top headlines in news.

                :param q_int_title: query term in title
                :param sources: source of news
                :param page_size: number of results to return per page request.
                In API - default = 20, maximum = 100
                :param from_param: from date
                :param to: to date
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:
        """
        try:
            if q_int_title:
                return self.news_api.get_everything(qintitle=self.query,
                                                    sources=sources,
                                                    page=page_no,
                                                    page_size=page_size,
                                                    from_param=from_param,
                                                    to=to)
            else:
                return self.news_api.get_everything(q=self.query,
                                                    sources=sources,
                                                    page=page_no,
                                                    page_size=page_size,
                                                    from_param=from_param,
                                                    to=to)
        except Exception as e:
            print(e)
        return None

    def get_top_headline_by_source(self, sources, page_no=1, page_size=100):
        """
                To fetch the top headlines in news by country

                :param sources: source of news
                :param page_size: number of results to return per page request.
                 In API - default = 20, maximum = 100
                :param page_no: to page through if the number of resultant page_size is more than expected
                :return:  json object
        """
        try:
            return self.news_api.get_top_headlines(source=sources,
                                                   page=page_no,
                                                   page_size=page_size)
        except Exception as e:
            print(e)
            return None
