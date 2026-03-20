with source as (
    SELECT * from {{ source('finance', 'raw_transactions')}}
),

renamed as (
    select
        user_id,
        date,
        year,
        month,
        year_month,
        monthly_income,
        monthly_expense_total,
        round(net_income::numeric,2) as net_income,
        savings_rate,
        actual_savings,
        budget_goal,
        financial_scenario,
        financial_stress_level,
        income_type,
        category,
        cash_flow_status,
        credit_score,
        debt_to_income_ratio,
        loan_payment,
        fraud_flag,
        savings_goal_met
    from source
)

select * from renamed