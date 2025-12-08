⭐ 1. ROW_NUMBER() — Most recent order per customer

```
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

```

---

⭐ 2. RANK() — Rank orders by amount per customer

```
SELECT
    o.customer_id,
    o.order_id,
    od.unit_price * od.quantity AS order_amount,
    RANK() OVER (
        PARTITION BY o.customer_id
        ORDER BY (od.unit_price * od.quantity) DESC
    ) AS amount_rank
FROM orders o
JOIN order_details od ON o.order_id = od.order_id;

```

---

⭐ 3. DENSE_RANK() — Rank products by price

```
SELECT
    product_id,
    product_name,
    unit_price,
    DENSE_RANK() OVER (
        ORDER BY unit_price DESC
    ) AS price_rank
FROM products;

```

---

⭐ 4. LAG() — Difference between consecutive orders

```
SELECT
    customer_id,
    order_date,
    LAG(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_date
FROM orders
ORDER BY customer_id, order_date;

```

---

⭐ 5. LEAD() — When the customer ordered next

```
SELECT
    customer_id,
    order_date,
    LEAD(order_date) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS next_order_date
FROM orders
ORDER BY customer_id, order_date;

```

---

⭐ 6. SUM() OVER — Running total of sales per customer

```
SELECT
    o.customer_id,
    o.order_date,
    od.unit_price * od.quantity AS amount,
    SUM(od.unit_price * od.quantity) OVER (
        PARTITION BY o.customer_id
        ORDER BY o.order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
ORDER BY customer_id, order_date;

```

---

⭐ 7. COUNT() OVER — How many orders each customer has

```
SELECT
    customer_id,
    COUNT(*) OVER (PARTITION BY customer_id) AS total_orders,
    order_id
FROM orders
ORDER BY customer_id, order_id;

```

---

⭐ 8. NTILE() — Bucket orders into quartiles by total amount

```
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

```

---

⭐ 9. FIRST_VALUE() — First product ordered by each customer

```
SELECT
    o.customer_id,
    o.order_id,
    FIRST_VALUE(o.order_id) OVER (
        PARTITION BY o.customer_id
        ORDER BY o.order_date
    ) AS first_order_id
FROM orders o
ORDER BY customer_id, order_date;

```

---

⭐ 10. LAST_VALUE() — Most recent product ordered (correct window frame)

```
SELECT
    o.customer_id,
    o.order_id,
    LAST_VALUE(o.order_id) OVER (
        PARTITION BY o.customer_id
        ORDER BY o.order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_order_id
FROM orders o
ORDER BY customer_id, order_date;
```




