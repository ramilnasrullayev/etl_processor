# ETL Processor



## Installation

1. Clone the repository:

   git clone https://github.com/ramilnasrullayev/etl_processor.git
   
   
2. Navigate to the project folder

   cd etl_processor
   
   
3.Install required dependencies 

   pip install -r requirements.txt


## Usage

1. Ensure you have the necessary input files in the data directory:

    train.csv: The training data file.
    test.csv: The test data file.
    
    Modify the main.py file if needed, specifying the correct file paths for the input and output files.

2. Run the ETL processing script:

    python main.py
    
    After the script finishes executing, the transformed data will be saved as data/test_transformed.csv
