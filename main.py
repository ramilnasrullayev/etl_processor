from project_etl_processor.etl_package import DataExtractor
from project_etl_processor.etl_package import DataTransformer
from project_etl_processor.etl_package import DataLoader


def main():
    train_file = 'train_data.csv'
    test_file = 'test_data.csv'
    output_file = 'test_transformed.csv'

    extractor = DataExtractor(train_file)
    train_data = extractor.extract_data()

    extractor = DataExtractor(test_file)
    test_data = extractor.extract_data()

    transformer = DataTransformer(train_data)
    transformed_data = transformer.process_data()

    loader = DataLoader(transformed_data, output_file)
    loader.load_data()

if __name__ == '__main__':
    main()
