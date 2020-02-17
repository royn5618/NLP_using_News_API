from NewsAPIClientCall import constants


class FetchData:
    def __init__(self, q, qInTitle, sources, domains, excludeDomains, from_date, to_date, sortBy, page_size, page,
                 api_key, category, lang, country):
        self.q = q
        self.qInTitle = qInTitle
        self.sources = sources
        self.domains = domains
        self.excludeDomains = excludeDomains
        self.from_date = from_date
        self.to_date = to_date
        self.sortBy = sortBy
        self.page_size = page_size
        self.page = page
        self.api_key = api_key
        self.category = category
        self.lang = lang
        self.country = country

    def fetch_top_headline(self):
        return news_api.get_top_headlines(q='bitcoin',
                                                  sources='bbc-news,the-verge',
                                                  category='business',
                                                  language='en',
                                                  country='us')

