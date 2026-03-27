with source as (
    SELECT * from {{ ref('stg_transactions')}}
),

monthly_spending as (
    select
        year_month,
        to_date(year_month || '-01', 'YYYY-MM-DD') as month_date,
        cast(replace(year_month, '-','') as integer) as year_month_sort,
        category,
        financial_scenario,
        sum(round(monthly_expense_total::numeric,2)) as monthly_expense
        from source
        group by year_month, to_date(year_month || '-01', 'YYYY-MM-DD'),
        cast(replace(year_month, '-', '') as integer),category, financial_scenario
)

select * from monthly_spending
order by year_month_sort