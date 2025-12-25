SELECT
    c.customer_id,
    p.product_name
FROM
    customers c
    LEFT OUTER JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_details d on o.order_id = d.order_id
    JOIN products p on d.product_id = p.product_id
where
    p.product_name = 'Tofu'
    -- AND c.customer_id IS NULL
order by
    c.customer_id
    -- select c.customer_id, SUM(d.quantity) as num_items_purchased
    -- group by c.customer_id
    -- having num_items_purchased > 1300
    -- order by num_items_purchased desc