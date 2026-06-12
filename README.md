# Phishing-URL-Detection
Machine Learning based phishing URL detection using Random Forest and URL feature extraction.

## Overview

Phishing attacks remain one of the most common cybersecurity threats, often tricking users into visiting malicious websites that mimic legitimate ones. The goal of this project is to build a machine learning model capable of identifying phishing URLs based on their characteristics and patterns.

The system analyzes various URL-based features and predicts whether a URL is legitimate or phishing, helping users avoid potentially harmful websites.

---

## Dataset

The model was trained using a dataset containing **549,362 URLs**, consisting of both legitimate and phishing websites.

The dataset includes URLs collected from multiple sources and labeled according to their legitimacy. Various URL-based attributes were extracted and used as input features for training the machine learning model.

### Dataset Characteristics

* Total URLs: **549,362**
* Classes:

  * Legitimate URLs
  * Phishing URLs
* Feature Type:

  * URL structure and lexical features
  * Domain-related features
  * Security-related indicators

Examples of extracted features include:

* URL length
* Number of dots (`.`)
* Number of special characters
* Presence of IP address in URL
* Use of HTTPS
* Number of subdomains
* Suspicious keywords in URL
* Domain-related information

---

## Methodology

### 1. Data Preprocessing

The collected dataset was first cleaned and prepared for training.

Steps performed:

* Removed duplicate entries
* Handled missing values
* Verified URL labels
* Converted extracted features into numerical format suitable for machine learning

### 2. Feature Extraction

Rather than analyzing webpage content, this project focuses on URL-based features that can be obtained instantly without visiting the website.

Feature extraction included:

* Lexical URL features
* Domain characteristics
* Security indicators
* Structural properties of URLs

These features help distinguish phishing URLs from legitimate ones based on common patterns observed in phishing attacks.

### 3. Model Training

The processed dataset was divided into training and testing sets.

The model was trained using the **Random Forest Classifier**, an ensemble learning algorithm that combines multiple decision trees to improve prediction performance and reduce overfitting.

### 4. Model Evaluation

After training, the model was evaluated on unseen test data using standard classification metrics such as:

* Accuracy
* Precision
* Recall
* F1 Score

The evaluation helped verify the model's ability to correctly identify phishing URLs while minimizing false predictions.

---

## Why Random Forest?

The Random Forest Classifier was chosen because:

* It performs well on large datasets.
* It can handle a large number of input features efficiently.
* It reduces overfitting compared to individual decision trees.
* It provides strong classification performance with minimal parameter tuning.
* It is robust against noisy and imbalanced data.
* It offers feature importance scores, helping identify which URL characteristics contribute most to phishing detection.

These advantages make Random Forest a reliable and practical choice for phishing URL classification.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

---

## Project Workflow

1. Collect phishing and legitimate URL datasets.
2. Extract meaningful URL-based features.
3. Preprocess and clean the data.
4. Split the dataset into training and testing sets.
5. Train a Random Forest Classifier.
6. Evaluate model performance.
7. Predict whether new URLs are phishing or legitimate.

---

## Future Scope

* Real-time URL scanning system
* Browser extension integration
* Web application deployment
* Continuous model retraining with updated phishing datasets
* Integration with threat intelligence feeds

---

## Conclusion

This project demonstrates how machine learning can be applied to cybersecurity problems by detecting phishing URLs through URL-based feature analysis. Using a dataset of over 549,000 URLs and a Random Forest Classifier, the system provides an efficient approach for identifying potentially malicious websites before users interact with them.

---

## Contributors

Developed as a group project by students of Computer Science and Engineering.
Team Members:
- Kinzal
- Kishan
- Khushi
- Kirti
- Krish

---

## My Contribution

My primary contributions included:

- Assisted in dataset preprocessing
- Performed feature engineering on URL attributes
- Worked on Random Forest model training
- Helped evaluate model performance
- Contributed to project documentation and GitHub repository management

---

## Learning Outcomes

Through this project, I gained hands-on experience with:
- Data preprocessing
- Feature extraction
- Machine learning workflows
- Classification models
- Collaborative software development
