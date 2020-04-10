import json
import os
import glob
from DataProcessor.DataParser import config
import datetime
from DataProcessor.NewsAPIGetData.constants import *


class Helper:

    @staticmethod
    def read_json(read_file_path, path):
        """
        Return list of jsons

        :param read_file_path:
        :param path:
        :return:
        """
        jsons = []
        for root, dirs, files in os.walk(path, topdown=True):
            if not files:
                continue
            else:
                for file in files:
                    full_path = root + '/' + file
                    print(full_path)
        pass

    @staticmethod
    def write_json(json_obj, query, country, source, date):
        """
        Folder structure:
        Data ->
                Query Term ->
                              Country ->
                                         Source ->
                                                    json_date.json

        :param json_obj: json object from newsAPI
        :param query: query term
        :param country: country
        :param source: source (only one source)
        :param date: date (only one date)
        :return
        """
        write_path = 'Data' + '/' + query + '/' + COUNTRY_MAP[country] + '/' + source
        if date:
            write_path = write_path + '/' + 'json_' + str(date).strip() + '.json'
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        with open(write_path, 'w') as outfile:
            json.dump(json_obj, outfile)
        print('Json Dumped at : ' + write_path)

    @staticmethod
    def convert_json_to_dataframe(write_file_path):
        pass

    @staticmethod
    def get_list_of_dates(num_days):
        """
        Generates list of dates

        :param num_days: Number of days to generate sequence of the dates
        :return: List of date range from today to the date in the gap of num_days
        """
        base = datetime.datetime.today()
        date_list = [(base - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(num_days)]
        return date_list

    @staticmethod
    def get_executed_q_terms():
        """
        Retrieves all query terms that were executed and stored. Retrieves from the sub-folder names of Data"
        :return: list of query terms already executed
        """
        q_terms_in_data_folder = []
        for root, dir_names, file_names in os.walk(config.DATA_PATH):
            q_terms_in_data_folder = dir_names
            break
        return q_terms_in_data_folder

    @staticmethod
    def verify_q_terms(query_list):
        """
        Returns if the query term(s) in the input argument exists in the Data
        :param query_list:list query term(s) in the input argument
        :return: True or False
        """
        # Get the folder names from Data
        all_q_terms = Helper.get_executed_q_terms()
        for query in query_list:
            if query in all_q_terms:
                continue
            else:
                raise ValueError("Query contents not in Data Folder")
        return True

