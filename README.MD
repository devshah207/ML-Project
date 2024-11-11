# Student Performance Prediction

This project is designed to predict students' math scores based on various demographic and academic factors. Using a dataset from [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977), the project utilizes a modular approach with distinct components for data ingestion, transformation, and model training. It also includes an interactive web application built with Flask, which allows users to explore predictions through a user-friendly interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Results](#results)
- [Future Work](#future-work)

## Project Overview

This project predicts the math score of students based on their performance in exams, parental level of education, test preparation, and other demographic factors. The solution includes exploratory data analysis (EDA), data preprocessing, model training and evaluation, hyperparameter tuning, and deployment of a Flask web application. Additionally, the project employs robust logging and exception handling to monitor processes and errors.

## Dataset

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977) and contains the following columns:
- **Gender**
- **Race/Ethnicity**
- **Parental Level of Education**
- **Lunch**
- **Test Preparation**
- **Math Score** (Target Variable)
- **Reading Score**
- **Writing Score**

## Project Structure

The project follows a modular structure, with separate components for each step of the ML pipeline. Here's an overview:

├── data_ingestion.py # Data ingestion component ├── data_transformation.py # Data preprocessing and transformation ├── model_training.py # Model training and evaluation ├── pipeline # Separate training and prediction pipelines ├── logger.py # Logging configuration to track changes and errors ├── exception.py # Custom exceptions for error handling ├── app.py # Flask web application for user interaction ├── templates/ # HTML files for Flask UI ├── static/ # CSS and JS for Flask UI ├── eda/ # EDA notebooks and visualizations ├── saved_models/ # Serialized models (.pkl files) ├── setup.py # Project setup file ├── requirements.txt # Required Python packages └── README.md # Project documentation


## Features

1. **Data Ingestion**: Loads the dataset from Kaggle or local sources.
2. **Data Transformation**: Preprocesses the dataset by handling null values, encoding categorical variables, scaling numerical features, and detecting outliers.
3. **Exploratory Data Analysis (EDA)**: Analyzes data distribution, identifies correlations, and performs feature engineering.
4. **Model Training**: Trains various machine learning models and optimizes them using Grid Search CV.
5. **Logging and Exception Handling**: Logs process changes and errors to a text file and tracks detailed exception messages, including file and line number.
6. **Model Persistence**: Saves the trained model as a `.pkl` file for future predictions.
7. **Web Application**: Provides a Flask-based user interface to make predictions on new data inputs.
8. **Automated Setup**: `setup.py` and `requirements.txt` allow easy installation of dependencies and setup.

## Installation

To run this project, clone the repository and install the dependencies:

```bash
git clone <repository_url>
cd StudentPerformancePrediction
pip install -r requirements.txt
python setup.py install

## Usage

### Train the Model
To train the model, use the following command:
```bash
python model_training.py

### Start the web app using: 
python app.py

## Model Evaluation
We tested multiple models (e.g., Linear Regression, Random Forest, Gradient Boosting) with hyperparameter tuning using Grid Search CV to find the best-performing model for predicting math scores. Evaluation metrics like MAE, MSE, and R² Score were used to assess model accuracy.

## Results
The best model achieved a high level of accuracy on the test dataset and is able to predict math scores effectively based on the features provided. The model is saved as a `.pkl` file, which can be loaded in the Flask application for real-time predictions.

## Future Work
- **Model Enhancement**: Experiment with additional advanced algorithms.
- **Feature Engineering**: Explore more feature engineering techniques to improve prediction accuracy.
- **Deployment**: Deploy the web application on cloud platforms (e.g., AWS, Heroku).
