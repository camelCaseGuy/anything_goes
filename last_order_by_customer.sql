SELECT
    customer_id,
    order_id,
    order_date,
    ROW_NUMBER() OVER (
        PARTITION BY
            customer_id
        ORDER BY
            order_date DESC
    ) AS rn
FROM
    orders
SELECT
    *
FROM
    (
        SELECT
            customer_id,
            order_id,
            order_date,
            ROW_NUMBER() OVER (
                PARTITION BY
                    customer_id
                ORDER BY
                    order_date DESC
            ) AS rn
        FROM
            orders
    ) t
WHERE
    rn = 1;