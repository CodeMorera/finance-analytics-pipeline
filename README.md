# Finance Analytics Pipeline
## About
An end-to-end finance analytics pipeline built with Python, PostgreSQL, dbt Core, and Power BI. It ingests synthetic personal finance data, cleans and validates it, transforms it into analytics-ready marts, and surfaces spending and income insights through an interactive BI dashboard.

## Business Value
This pipeline turns raw finance data into analytics-ready datasets that make it easier to monitor spending patterns, compare economic scenarios, and track income, expenses, and running balances over time.

## Key Features
- Cleaned and loaded 3,000 synthetic finance records into PostgreSQL using Python and SQLAlchemy
- Built dbt staging and mart models for spending, category summaries, and income vs. expense analysis
- Added 23 passing dbt tests for data quality and model validation
- Created Power BI dashboards for spending trends, category analysis, net income, and running balance
- Modeled multiple economic scenarios: normal, inflation, and recession

## Tech Stack
- Python (pandas, SQLAlchemy)
- PostgreSQL
- dbt Core
- Power BI
- Git / GitHub

## Project Architecture
Raw CSV → Python Cleaning → PostgreSQL → dbt Models → Power BI Dashboard

## Lineage Graph
![dbt Lineage Graph showing raw_transactions flowing through stg_transactions to three mart models](image-1.png)

## Dashboard
### Spending Overview
![Power BI dashboard showing total spend by category and monthly expense trends](dashboard_page1.png)

### Income vs Expense
![Power BI dashboard showing income vs expense over time and running balance](dashboard_page2.png)

## Setup Instructions
### 1. Clone the repo
```bash
git clone https://github.com/CodeMorera/finance-analytics-pipeline.git
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv/Scripts/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file in the root folder with:
```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=finance_db
```

### 5. Run the pipeline
```bash
python src/clean.py
python src/load.py
```

### 6. Run dbt models
```bash
cd finance_dbt
dbt run
dbt test
```
## dbt Models

### Staging
- `stg_transactions`: cleaned and standardized transaction-level source data

### Marts
- `monthly_spending`: monthly spending by category and scenario
- `category_summary`: aggregated spending by category
- `income_vs_expense`: income, expense, net income, and running balance over time

## Data Source
Synthetic personal finance dataset from Kaggle with 3,000 records spanning 2019–2023 across normal, inflation, and recession economic scenarios. 100% privacy-safe synthetic data.


