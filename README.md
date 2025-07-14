# Machine Learning Projects Portfolio 🤖

A comprehensive collection of machine learning projects focusing on financial and real estate data analysis, including loan default prediction, credit card fraud detection, and Airbnb market analysis.

## 📋 Project Overview

This repository contains multiple machine learning projects showcasing various ML techniques and applications:

### 🏦 1. Loan Default Prediction
**Main Project** - Predicting loan approval status using customer financial data
- **Dataset**: 613 records with 13 attributes
- **Objective**: Binary classification to predict loan approval
- **Models**: XGBoost, Random Forest, Decision Tree, Logistic Regression
- **Key Features**: Credit history, income, loan amount, property area

### 💳 2. Credit Card Fraud Detection
Advanced fraud detection system using transaction data
- **Objective**: Identify fraudulent credit card transactions
- **Techniques**: Anomaly detection and supervised learning
- **Focus**: Handling imbalanced datasets and feature engineering

### 🏠 3. Airbnb Market Analysis (2 Versions)
Comprehensive analysis of Airbnb rental market data
- **Version 1**: Initial exploratory data analysis and price prediction
- **Version 2**: Enhanced model with additional features and improved accuracy
- **Dataset**: Adult.csv (demographic and economic data)
- **Applications**: Price optimization and market insights

## 🗂️ Project Structure

```
ML-loan_default_Prediction/
├── 📁 data/                    # Datasets
│   ├── train_loan.csv         # Loan training data
│   ├── test_loan.csv          # Loan test data
│   └── adult.csv              # Adult demographic data
├── 📁 notebooks/              # Jupyter notebooks
│   ├── 01_loan_default_prediction.ipynb
│   ├── 02_credit_card_fraud_detection.ipynb
│   ├── 03_airbnb_analysis_v1.ipynb
│   └── 04_airbnb_analysis_v2.ipynb
├── 📁 docs/                   # Documentation
│   └── Machine_Learning_Project_Brief.pdf
├── config.py                 # Data path configuration
├── data_loader.py            # Data loading utilities
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
├── SETUP_NOTES.md           # Important setup instructions
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ML-loan_default_Prediction.git
   cd ML-loan_default_Prediction
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv ml_env
   source ml_env/bin/activate  # On Windows: ml_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Update notebook paths** (Important!)
   ```bash
   # Check that data files are accessible
   python config.py
   ```
   
   ⚠️ **Note**: The notebooks contain hardcoded file paths that need updating. See `SETUP_NOTES.md` for detailed instructions.

5. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

## 📊 Key Features & Techniques

### Machine Learning Algorithms
- **XGBoost**: Gradient boosting for high performance
- **Random Forest**: Ensemble method for robust predictions
- **Logistic Regression**: Linear classification baseline
- **Decision Trees**: Interpretable classification models

### Data Science Techniques
- **Exploratory Data Analysis (EDA)**: Comprehensive data understanding
- **Feature Engineering**: Creating meaningful predictors
- **Data Preprocessing**: Handling missing values and encoding
- **Model Evaluation**: Cross-validation and performance metrics
- **Visualization**: Advanced plotting with matplotlib, seaborn, and plotly

### Statistical Analysis
- Correlation analysis
- Distribution analysis
- Outlier detection and treatment
- Feature selection and importance

## 📈 Project Highlights

### Loan Default Prediction
- **Accuracy**: Achieved high classification accuracy using ensemble methods
- **Features**: Leveraged credit history, income ratios, and demographic data
- **Business Impact**: Direct application in financial risk assessment

### Credit Card Fraud Detection
- **Challenge**: Highly imbalanced dataset requiring specialized techniques
- **Solution**: Advanced sampling methods and anomaly detection
- **Real-world Application**: Critical for financial security systems

### Airbnb Analysis
- **Market Insights**: Comprehensive pricing and demand analysis
- **Predictive Modeling**: Price optimization recommendations
- **Business Value**: Strategic insights for property investors and hosts

## 🛠️ Technologies Used

- **Programming**: Python 3.x
- **Data Analysis**: Pandas, NumPy
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Development**: Jupyter Notebook
- **Statistical Analysis**: SciPy, Statsmodels

## 📚 Learning Outcomes

This portfolio demonstrates proficiency in:
- End-to-end machine learning pipeline development
- Multiple domain applications (finance, real estate, fraud detection)
- Model selection and hyperparameter optimization
- Data visualization and storytelling
- Business problem solving through data science

## 👥 Authors

**Kindi Diallo**
- Machine Learning Projects Portfolio
- Academic Year: 2021

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📞 Contact

For questions or collaboration opportunities, please reach out through GitHub issues or pull requests.

---

⭐ **Star this repository if you find it helpful!** ⭐