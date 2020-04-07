import json
import os
from datetime import date

class Helper:

    @staticmethod
    def read_json(read_file_path):
        pass

    @staticmethod
    def read_json_to_dataframe(read_file_path):
        pass

    @staticmethod
    def write_json(json_obj, query, country):
        write_path = 'Data' + '/' + query
        if country:
            write_path = write_path + '/' + country
        write_path = write_path + '/' +  'json_' + str(date.today().strftime("%d_%b_%Y")) + '.json'
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        with open(write_path, 'w') as outfile:
            json.dump(json_obj, outfile)
        print('Json Dumped at : ' + write_path)

    @staticmethod
    def write_json_to_dataframe(write_file_path):
        pass
