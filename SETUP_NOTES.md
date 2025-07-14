# Setup Notes

## Important: Updating Notebook File Paths

The original notebooks contain hardcoded file paths that need to be updated for your local environment. Here's how to fix them:

### Quick Fix for All Notebooks

Instead of using hardcoded paths, use the provided data loader utilities:

```python
# At the beginning of any notebook, add:
import sys
sys.path.append('..')  # Go up one level to project root
from data_loader import load_loan_data, load_adult_data, load_credit_card_data

# Then load data like this:
train_df, test_df = load_loan_data()
```

### Specific Updates Needed

#### 1. Loan Prediction Notebook (`01_loan_default_prediction.ipynb`)

Replace these hardcoded paths:
```python
# OLD (remove these):
tr_path = "/Users/[username]/path/to/train_loan.csv"
te_path = "/Users/[username]/path/to/test_loan.csv"

# NEW (use this instead):
from data_loader import load_loan_data
train_df, test_df = load_loan_data()
```

#### 2. Credit Card Fraud Detection Notebook (`02_credit_card_fraud_detection.ipynb`)

Replace:
```python
# OLD:
ccard = pd.read_csv('/Users/[username]/path/to/creditcard.csv')

# NEW:
from data_loader import load_credit_card_data
ccard = load_credit_card_data()
```

Note: You'll need to download the credit card dataset from [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud) and place it in the `data/` folder.

#### 3. Airbnb Analysis Notebooks (`03_airbnb_analysis_v1.ipynb`, `04_airbnb_analysis_v2.ipynb`)

Replace any hardcoded paths with:
```python
from data_loader import load_adult_data
adult_df = load_adult_data()
```

### File Structure Expected

```
ML-loan_default_Prediction/
├── data/
│   ├── train_loan.csv     ✓ (included)
│   ├── test_loan.csv      ✓ (included)
│   ├── adult.csv          ✓ (included)
│   └── creditcard.csv     ⚠️ (download separately)
├── notebooks/
│   └── [your notebooks]
├── config.py              ✓ (included)
└── data_loader.py         ✓ (included)
```

### Testing Your Setup

Run this to verify everything is working:

```bash
python config.py
python data_loader.py
```

This will check if all data files are found and accessible. 