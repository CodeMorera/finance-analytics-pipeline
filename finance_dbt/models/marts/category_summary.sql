with source as (
    SELECT * from {{ ref('stg_transactions')}}
),

category_summary as (
    select
        category,
        round(sum(monthly_expense_total::numeric),2) as total_spend,
        round(avg(monthly_expense_total::numeric),2) as avg_spend,
        round(
            (100.0 * sum(monthly_expense_total::numeric)
            /sum(sum(monthly_expense_total::numeric)) over ())::numeric,
            2
            ) as percentage
        from source
        group by category
)

select * from category_summary
order by total_spend desc