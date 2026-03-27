# Finance Analytics Pipeline

A data pipeline that cleans, loads, and models personal finance data 
using Python, PostgreSQL, dbt, and Power BI.

## Tech Stack
- Python (pandas, SQLAlchemy)
- PostgreSQL
- dbt Core
- Power BI
- Git / GitHub

## Project Architecture
Raw CSV → Python Cleaning → PostgreSQL → dbt Models → Power BI Dashboard

## Lineage Graph
![alt text](image-1.png)

## Dashboard
### Spending Overview
![alt text](dashboard_page1.png)

### Income vs Expense
![alt text](dashboard_page2.png)

## Setup Instructions
### 1. Clone the repo
git clone https://github.com/CodeMorera/finance-analytics-pipeline.git

### 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create a .env file in the root folder with:
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=finance_db

### 5. Run the pipeline
python src/clean.py
python src/load.py

## Status
- [x] Week 1 — Repo setup
- [x] Week 2 — Data cleaning script
- [x] Week 3 — PostgreSQL loading with assertions
- [x] Week 4 — dbt models
- [x] Week 5 — dbt mart models
- [x] Week 6 — dbt tests and documentation
- [x] Week 7 — Power BI dashboard
