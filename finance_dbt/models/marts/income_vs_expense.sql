--Create models/marts/income_vs_expense.sql — monthly net 
--(income minus expenses) and running balance using a window function (SUM() OVER)

with source as (
    SELECT * from {{ ref('stg_transactions')}}
),

income_vs_summary as (
    select
        year_month,
        round(sum(monthly_income::numeric), 2) as total_income,
        round(sum(monthly_expense_total::numeric), 2) as total_expense,
        round(sum(net_income::numeric),2) as net_income
        from source
        group by year_month
)
select
    year_month,
    total_income,
    total_expense,
    net_income,
    round(
        sum(net_income) over (
            order by year_month
            rows between unbounded preceding and current row
        ),
        2
    ) as running_balance

from income_vs_summary
order by year_month