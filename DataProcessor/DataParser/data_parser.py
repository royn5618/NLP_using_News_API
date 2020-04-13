import os

import pandas as pd
from pandas.io.json import json_normalize

from DataProcessor.DataParser import constants
from DataProcessor.DataParser.config import *
from helper_functions import Helper


class DataParser:

    def __init__(self, q_terms):
        """

        :param q_terms:list query terms to process

        """
        self.q_terms = q_terms
        self.df = pd.DataFrame()

    def get_data_frame_from_json(self):
        """
        Parses iteratively the jsons in folders and returns a complete Pandas DataFrame.
        :return: Pandas DataFrame
        """
        for query in self.q_terms:
            print("Collecting for:" + query)
            for root, dir_nms, file_nms in os.walk(DATA_PATH + query):
                for dir_nm in dir_nms:
                    country = dir_nm
                    print("Collecting for:" + country)
                    for new_root, new_dir_nm, new_file_nms in os.walk(root + '/' + dir_nm):
                        if new_file_nms:
                            for new_file_nm in new_file_nms:
                                # print("Collecting for:" + new_file_nm)
                                json_file = Helper.read_json(new_root + '/' + new_file_nm)
                                df_daily = json_normalize(json_file[constants.JSON_ARTICLE_OBJ])
                                # print(df_daily.columns)
                                if len(df_daily):
                                    df_daily.drop(columns=constants.COLS_TO_DROP, inplace=True)
                                    df_daily['country'] = country
                                self.df = pd.concat([self.df, df_daily])
                break
        return self.df
