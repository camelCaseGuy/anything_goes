SELECT
    c.customer_id,
    o.order_date
FROM
    customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE
    o.order_date IS NULL