import json
import os
import datetime
from datetime import date

class Helper:

    @staticmethod
    def read_json(read_file_path):
        pass

    @staticmethod
    def read_json_to_dataframe(read_file_path):
        pass

    @staticmethod
    def write_json(json_obj, query, country, date=None):
        write_path = 'Data' + '/' + query
        if country:
            write_path = write_path + '/' + country + '/Monthly/the_irish_times'
        if date:
            write_path = write_path + '/' + 'json_' + str(date).strip() + '.json'
        else:
            write_path = write_path + '/' + 'json_' + str(date.today().strftime("%d_%b_%Y")) + '.json'
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        with open(write_path, 'w') as outfile:
            json.dump(json_obj, outfile)
        print('Json Dumped at : ' + write_path)

    @staticmethod
    def write_json_to_dataframe(write_file_path):
        pass

    @staticmethod
    def get_list_of_dates(num_days):
        base = datetime.datetime.today()
        date_list = [(base - datetime.timedelta(days=x)).strftime("%Y-%m-%d") for x in range(num_days)]
        return date_list

