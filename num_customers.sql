SELECT
    country,
    COUNT(customer_id) as num_customers
FROM
    customers
group by
    country
HAVING
    country is not null
order by
    num_customers DESC