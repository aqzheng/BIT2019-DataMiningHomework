import pandas as pd
import os
from config import data_path, data_file_list

def makedir(path):
	if not os.path.exists(path):
		os.makedirs(path)

class Data():
    def __init__(self):
        self.read_data = os.path.join("data", data_path)
        self.write_data = os.path.join("result", data_path)
        self.data_file_list = data_file_list

    def process_features(self):
        for file_name in self.data_file_list:
            content = pd.read_csv(os.path.join(self.read_data, file_name))
            write_data_path = os.path.join(self.write_data, file_name.split('.')[0])
            makedir(write_data_path)
            print("--------------------------------------------------------------------------------------------------------------")
            print("Begin to process file: %s" % file_name)
            for title in content.columns.values:
                if content[title].dtypes == "int64" or content[title].dtypes == "float64":
                   content = content.drop(columns = [title])
            content = content.dropna()
            with open(os.path.join(write_data_path, 'processd.csv'), 'w', encoding = 'utf-8') as fp:
                content.to_csv(fp)
     
if __name__ == '__main__':
    data = Data()
    
    data.process_features()
