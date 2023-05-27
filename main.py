from etl_package import *

def main():
    train_file = 'data/train.csv'
    test_file = 'data/test.csv'
    output_file = 'data/test_transformed.csv'

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
