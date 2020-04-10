from DataProcessor.DataParser.constants import *


import pandas as pd


class DataParser:

    def __init__(self, json, q_term, country):
        """

        :param json:
        :param q_term:
        :param country:
        """

        self.json = json
        self.country = country
        self.source = None
        self.author = None
        self.title = None
        self.description = None
        self.url = None
        self.published_at=None
        self.url_to_image= None
        self.content = None
        self.df = pd.DataFrame(columns=COLUMNS)

    def get_json_list(self):
        pass

    def unravel_json(self):
        pass
