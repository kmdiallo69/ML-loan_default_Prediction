"""
Configuration file for ML project data paths
Update these paths according to your local setup
"""

import os

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Data file paths
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Loan prediction datasets
TRAIN_LOAN_PATH = os.path.join(DATA_DIR, 'train_loan.csv')
TEST_LOAN_PATH = os.path.join(DATA_DIR, 'test_loan.csv')

# Adult dataset for Airbnb analysis
ADULT_DATA_PATH = os.path.join(DATA_DIR, 'adult.csv')

# For credit card fraud detection - you'll need to download this dataset
# from Kaggle: https://www.kaggle.com/mlg-ulb/creditcardfraud
CREDIT_CARD_PATH = os.path.join(DATA_DIR, 'creditcard.csv')

# Verify data files exist
def check_data_files():
    """Check if required data files exist"""
    files_to_check = [
        ('Training loan data', TRAIN_LOAN_PATH),
        ('Test loan data', TEST_LOAN_PATH),
        ('Adult dataset', ADULT_DATA_PATH),
    ]
    
    print("Checking data files...")
    for name, path in files_to_check:
        if os.path.exists(path):
            print(f"✓ {name}: Found")
        else:
            print(f"✗ {name}: Missing - {path}")
    
    # Credit card data is optional as it needs to be downloaded separately
    if os.path.exists(CREDIT_CARD_PATH):
        print(f"✓ Credit card data: Found")
    else:
        print(f"! Credit card data: Not found (download from Kaggle if needed)")

if __name__ == "__main__":
    check_data_files() 