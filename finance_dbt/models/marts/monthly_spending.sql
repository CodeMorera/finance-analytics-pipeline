with source as (
    SELECT * from {{ ref('stg_transactions')}}
),

monthly_spending as (
    select
        year_month,
        category,
        sum(round(monthly_expense_total::numeric,2)) as monthly_expense
        from source
        group by year_month, category
)

select * from monthly_spending
order by year_month