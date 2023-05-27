import pandas as pd



class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_data(self):
        return pd.read_csv(self.file_path)
    

class DataTransformer:
    def __init__(self, train_data,test_data, factor_type='1'):
        self.train_data = train_data
        self.test_data = test_data
        self.factor_type = factor_type
        self.feature_columns = [col for col in self.test_data.columns if col.startswith('feature_type_1')]

    def standardize_features(self):
        for col in self.feature_columns:
            mean = self.train_data[col].mean()
            std = self.train_data[col].std()
            self.test_data[col] = (self.test_data[col] - mean) / std

    def compute_max_feature_index(self):
        self.test_data['max_feature_type_1_index'] = self.test_data[self.feature_columns].idxmax(axis=1)
        self.test_data['max_feature_type_1_index'] = self.test_data['max_feature_type_1_index'].apply(lambda x: int(x.split('_')[-1]))

    def process_data(self):
        self.compute_max_feature_index()
        self.standardize_features()
        return self.test_data



class DataLoader:
    def __init__(self, data, output_file):
        self.data = data
        self.output_file = output_file

    def load_data(self):
        self.data.to_csv(self.output_file, index=False)