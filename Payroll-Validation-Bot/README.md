Payroll Validation Bot

Project Overview

The Payroll Validation Bot is an automated payroll auditing system developed using Python, Pandas, and Streamlit.

The system reads payroll data from a CSV file, validates employee records, detects payroll anomalies, and generates an exception report for HR Managers.

Features

- Reads payroll data from CSV files
- Detects missing fields
- Detects duplicate Employee IDs
- Detects sudden salary jumps
- Generates an exception report
- Displays results using Streamlit

Technologies Used

- Python
- Pandas
- Streamlit
- VS Code

Dataset

The dataset was downloaded from Kaggle and used for payroll validation testing.

Dataset Columns:

- EmployeeID
- Name
- Department
- Experience_Years
- Education_Level
- Age
- Gender
- City
- Monthly_Salary
- Previous_Month_Salary

Validation Checks

1. Missing Field Validation

The system identifies records with missing EmployeeID, Name, Department, or Monthly_Salary values.

2. Duplicate Employee ID Validation

The system detects duplicate Employee IDs within the payroll dataset.

3. Sudden Salary Jump Validation

The system compares Previous_Month_Salary with Monthly_Salary and flags employees whose salary increase exceeds the defined threshold.

Output

The system generates an exception report containing:

- Missing Fields
- Duplicate Employee IDs
- Sudden Salary Jumps

The exception report is automatically saved in:

reports/exception_report.csv

Run the Application

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Result

The Payroll Validation Bot successfully validates payroll records and generates exception reports for HR review.