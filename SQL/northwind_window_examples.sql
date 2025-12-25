-- Window function examples for a Northwind-style schema (PostgreSQL).

-- 1. Most recent order per customer
SELECT *
FROM (
    SELECT
        customer_id,
        order_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC
        ) AS rn
    FROM orders
) t
WHERE rn = 1;


-- 2. Rank orders by total amount per customer
SELECT
    o.customer_id,
    o.order_id,
    SUM(od.unit_price * od.quantity) AS order_amount,
    RANK() OVER (
        PARTITION BY o.customer_id
        ORDER BY SUM(od.unit_price * od.quantity) DESC
    ) AS amount_rank
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.customer_id, o.order_id;


-- 3. Bucket orders into quartiles by total amount
SELECT
    o.order_id,
    SUM(od.unit_price * od.quantity) AS total_amount,
    NTILE(4) OVER (
        ORDER BY SUM(od.unit_price * od.quantity)
    ) AS quartile
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.order_id
ORDER BY total_amount;
