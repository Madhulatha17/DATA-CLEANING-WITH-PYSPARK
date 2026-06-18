# DATA-CLEANING-WITH-PYSPARK

##  Project Overview

This project demonstrates **data cleaning and preprocessing using PySpark**, a Big Data processing framework.

The goal is to handle:
- Missing values  
- Duplicate records  
- Data type corrections  

and produce a clean dataset for further analysis.


##  Objective

To build a scalable data cleaning pipeline using PySpark that can process large datasets efficiently.



##  Features

- Load CSV dataset using PySpark  
- Remove duplicate records  
- Handle missing values  
- Type conversion and preprocessing  
- Save cleaned dataset  



##  Data Cleaning Steps

1. Load dataset using Spark DataFrame  
2. Identify and remove duplicates  
3. Handle missing values using fillna()  
4. Convert incorrect data types  
5. Store cleaned dataset  



## Dataset Description

| Column | Description |
|--------|-------------|
| id     | Unique ID |
| name   | Employee Name |
| age    | Age (may contain missing values) |
| salary | Salary (may contain missing values) |



##  How to Run

### 1. Install dependencies
bash
pip install pyspark

### Technologies used
Python
PySpark
Big Data Processing
