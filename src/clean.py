import pandas as pd

def main():
    df = pd.read_csv('..\\data\\raw\\personal_finance_tracker_dataset.csv')
    df = df.drop_duplicates()
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['year_month'] = df['date'].dt.to_period('M').astype(str)
    df['financial_stress_level'] = df['financial_stress_level'].str.strip().str.lower()
    df['income_type'] = df['income_type'].str.strip().str.lower()
    df['category'] = df['category'].str.strip().str.lower()
    df['cash_flow_status'] = df['cash_flow_status'].str.strip().str.lower()
    df['net_income'] = df['monthly_income'] - df['monthly_expense_total']
    df['credit_score'] = df['credit_score'].astype('Int64')

    assert df['net_income'].isnull().sum() == 0
    assert df['monthly_income'].min() > 0, "Negative income found"
    assert df['financial_scenario'].isin(['normal', 'inflation', 'recession']).all(), "Unexpected scenario values"
    assert len(df) > 0, "DataFrame is empty"
    print(f"Clean complete. Rows: {len(df)}")

    df.to_csv('..\\data\\cleaned\\transactions_clean.csv', index=False)

main()