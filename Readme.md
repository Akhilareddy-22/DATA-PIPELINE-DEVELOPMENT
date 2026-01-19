# Data Pipeline Development - Internship Task 1

## Project Overview
This project implements a simple data pipeline using Python. The pipeline performs data preprocessing, transformation, and loading (ETL) using Pandas and Scikit-learn.

The goal is to clean raw CSV data and prepare it for machine learning or analysis.

## Features
- Reads raw dataset from CSV file
- Handles categorical and numerical data
- Converts text columns into numeric values using Label Encoding
- Scales numerical columns using Standard Scaler
- Saves cleaned and transformed data into a new CSV file
- Fully automated ETL pipeline

## Technologies Used
- Python
- Pandas
- Scikit-learn
- VS Code

## How to Run the Project

1. Install required libraries:
```bash
pip install -r requirements.txt

2.Run the pipeline 
python data_pipeline.py

3.Output file will be generated as 
cleaned_data.csv