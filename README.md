Credit Card Fraud Detection System

A Machine Learning-based system that detects potentially fraudulent credit card transactions using classification algorithms and handles the highly imbalanced nature of fraud detection datasets.

Project Overview

Credit card fraud detection is a binary classification problem where fraudulent transactions represent only a small percentage of total transactions.

This project builds an end-to-end Machine Learning pipeline to:

- Preprocess transaction data
- Handle class imbalance
- Train fraud classification models
- Evaluate model performance using fraud-focused metrics
- Save the trained model for reuse
- Provide a simple interface for predicting whether a transaction is fraudulent

Features

- Transaction fraud classification
- Handling of highly imbalanced data
- Exploratory Data Analysis
- Machine Learning classification
- Precision, Recall and F1-score evaluation
- ROC-AUC and Precision-Recall AUC
- Confusion Matrix visualization
- Random Forest feature importance
- Model serialization using Joblib
- Streamlit-based prediction interface

Technologies Used

Technology| Purpose
Python| Core programming language
Pandas| Data manipulation
NumPy| Numerical operations
Scikit-learn| Machine Learning
Matplotlib| Data visualization
Seaborn| Statistical visualization
Joblib| Model saving and loading
Streamlit| Web-based prediction interface

Machine Learning Models

1. Logistic Regression

Logistic Regression is used as a baseline classification model.

Class weighting is used to give greater importance to the minority fraud class.

2. Random Forest

Random Forest is an ensemble learning algorithm consisting of multiple decision trees.

The model is configured to handle class imbalance using class weights.

Machine Learning Pipeline

Raw Transaction Data
        |
        v
Data Preprocessing
        |
        v
Exploratory Data Analysis
        |
        v
Feature Scaling
        |
        v
Train/Test Split
        |
        v
Handle Class Imbalance
        |
        v
Train ML Models
        |
        v
Model Evaluation
        |
        v
Save Trained Model
        |
        v
Fraud Prediction

Dataset

The dataset contains transaction-related features including:

- "Time"
- "Amount"
- "V1" to "V28"
- "Class"

The target variable is:

Class = 0 -> Legitimate Transaction
Class = 1 -> Fraudulent Transaction

«Note: If this repository uses the synthetic dataset created for development and testing, the dataset is synthetic and should not be interpreted as real-world banking transaction data.»

For a production-oriented implementation, a publicly available benchmark dataset can be used instead.

Installation

Clone the repository:

git clone https://github.com/Simrangupta185/Credit-Card-Fraud-Detection-System.git

Navigate to the project directory:

cd Credit-Card-Fraud-Detection-System

Install the required dependencies:

pip install -r requirements.txt

Project Structure

Credit-Card-Fraud-Detection-System/
|
├── data/
│   └── creditcard.csv
|
├── models/
│   └── fraud_model.pkl
|
├── train.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

Train the Model

Make sure the dataset is located at:

data/creditcard.csv

Run the training script:

python train.py

The training script performs the following steps:

1. Loads the dataset
2. Preprocesses the transaction data
3. Scales the "Time" and "Amount" features
4. Splits the dataset into training and testing sets
5. Trains the classification models
6. Generates evaluation metrics
7. Saves the trained model

The trained model is saved as:

models/fraud_model.pkl

Run the Prediction Application

After training the model, start the Streamlit application:

streamlit run app.py

The application allows users to enter transaction features and receive a fraud prediction.

Example output:

Transaction Status:
Potential Fraud

or:

Transaction Status:
Legitimate Transaction

The application also displays the estimated probability of the transaction being fraudulent.

Model Evaluation

Fraud detection datasets are generally highly imbalanced, so accuracy alone is not sufficient for evaluating the model.

This project uses the following evaluation metrics:

- Precision
- Recall
- F1-Score
- ROC-AUC
- Precision-Recall AUC
- Confusion Matrix

Precision

Precision measures how many transactions predicted as fraudulent are actually fraudulent.

Recall

Recall measures how many actual fraudulent transactions are successfully detected.

F1-Score

F1-Score provides a balance between precision and recall.

ROC-AUC

ROC-AUC measures the model's ability to distinguish between fraudulent and legitimate transactions across different classification thresholds.

Precision-Recall AUC

PR-AUC is particularly useful when working with highly imbalanced classification datasets.

Fraud Detection Considerations

A fraud detection system needs to consider both false positives and false negatives.

False Positive

Legitimate Transaction -> Predicted as Fraud

False Negative

Fraudulent Transaction -> Predicted as Legitimate

Reducing false negatives is an important consideration because undetected fraudulent transactions can result in financial losses.

Future Improvements

Potential improvements to the project include:

- Hyperparameter optimization
- XGBoost or LightGBM implementation
- SMOTE-based oversampling
- Classification threshold optimization
- Real-time transaction monitoring
- Explainable AI using SHAP
- REST API deployment
- Cloud deployment
- Database integration
- Transaction monitoring dashboard
- Model drift detection

Learning Outcomes

This project provided practical experience with:

- Binary classification
- Imbalanced datasets
- Feature scaling
- Exploratory Data Analysis
- Ensemble Machine Learning
- Model evaluation
- Fraud detection concepts
- Model serialization
- Streamlit application development
- End-to-end Machine Learning workflows

Author

Simran Gupta

B.Tech - Computer Science and Engineering

GitHub:
https://github.com/Simrangupta185

License

This project is intended for educational and demonstration purposes.

Disclaimer

This project is not designed to make real financial decisions or replace production-grade banking fraud detection systems.
