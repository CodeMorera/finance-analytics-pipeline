with source as (
    SELECT * from {{ ref('monthly_spending')}}
),

category_summary as (
    select
        category,
        round(sum(monthly_expense::numeric),2) as total_spend,
        round(avg(monthly_expense::numeric),2) as avg_spend,
        round(
            100.0 * sum(monthly_expense::numeric)
            /sum(sum(monthly_expense)) over (),
            2
            ) as percentage
        from source
        group by category
)

select * from category_summary
order by total_spend desc