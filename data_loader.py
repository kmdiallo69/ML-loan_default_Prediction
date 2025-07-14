"""
Data loader utility for ML projects
Use this instead of hardcoded paths in your notebooks
"""

import pandas as pd
import os
from config import TRAIN_LOAN_PATH, TEST_LOAN_PATH, ADULT_DATA_PATH, CREDIT_CARD_PATH

def load_loan_data():
    """Load loan prediction datasets"""
    try:
        train_df = pd.read_csv(TRAIN_LOAN_PATH)
        test_df = pd.read_csv(TEST_LOAN_PATH)
        print(f"Training set loaded: {train_df.shape}")
        print(f"Test set loaded: {test_df.shape}")
        return train_df, test_df
    except FileNotFoundError as e:
        print(f"Error loading loan data: {e}")
        print("Make sure the data files are in the 'data/' directory")
        return None, None

def load_adult_data():
    """Load adult dataset for Airbnb analysis"""
    try:
        adult_df = pd.read_csv(ADULT_DATA_PATH)
        print(f"Adult dataset loaded: {adult_df.shape}")
        return adult_df
    except FileNotFoundError as e:
        print(f"Error loading adult data: {e}")
        return None

def load_credit_card_data():
    """Load credit card fraud detection dataset"""
    try:
        cc_df = pd.read_csv(CREDIT_CARD_PATH)
        print(f"Credit card dataset loaded: {cc_df.shape}")
        return cc_df
    except FileNotFoundError as e:
        print(f"Credit card data not found: {e}")
        print("Download from: https://www.kaggle.com/mlg-ulb/creditcardfraud")
        return None

# Example usage for notebooks:
if __name__ == "__main__":
    print("Testing data loaders...")
    
    # For loan prediction notebook:
    train_df, test_df = load_loan_data()
    
    # For Airbnb analysis:
    adult_df = load_adult_data()
    
    # For credit card fraud detection:
    cc_df = load_credit_card_data() 