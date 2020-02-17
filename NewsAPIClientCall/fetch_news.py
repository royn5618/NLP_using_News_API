from NewsAPIClientCall import constants


class FetchData:
    def __init__(self, news_api):
        """
        :param news_api: news api client object
        """""
        self.news_api = news_api

    def fetch_top_headline(self, query, sources, category, country, page_size, page, lang=constants.DEFAULT_LANG):
        """
        To fetch the top headlines in news.

        :param query: query term / keyword
        :param sources: comma-separated string of sources
        :param category: category of news
        :param country: 2-letter ISO 3166-1 code of the country
        :param page_size: number of results to return per page request. default = 20, maximum = 100
        :param page: to page through if the number of resultant page_size is more than expected
        :param lang: language, default = all languages
        :return:
        """
        return self.news_api.get_top_headlines(q=query,
                                               sources=sources,
                                               category=category,
                                               language=lang,
                                               country=country,
                                               page=page,
                                               page_size=page_size)

    def fetch_everything_by_page(self, query, q_in_title, sources,domains,
                                 exclude_domains, from_date, to_date,
                                 sort_by, page_size, page,
                                 lang=constants.DEFAULT_LANG):
        """
        To fetch the news sources and blogs available in the newsapi
        :param query: query term / keyword
        :param q_in_title: query term / keyword to search in title
        :param sources: comma-separated string of sources
        :param domains:
        :param exclude_domains:
        :param from_date:
        :param to_date:
        :param sort_by:
        :param page_size: number of results to return per page request. default = 20, maximum = 100
        :param page: to page through if the number of resultant page_size is more than expected
        :param lang: language, default = all languages
        :return:
        """
        return self.news_api.get_everything(q=query,
                                            qintitle=q_in_title,
                                            sources=sources,
                                            domains=domains,
                                            excludeDomains=exclude_domains,
                                            from_param=from_date,
                                            to=to_date,
                                            language=lang,
                                            sort_by=sort_by,
                                            page_size=page_size,
                                            page=page
                                            )

    def fetch_sources(self, category, country, lang=constants.DEFAULT_LANG):
        """
        To fetch the publishers available on the newsapi

        :param category: category of news
        :param country: 2-letter ISO 3166-1 code of the country
        :param lang: language, default = all languages
        :return:
        """
        return self.news_api.get_sources(category=category,
                                         language=lang,
                                         country=country
                                         )

