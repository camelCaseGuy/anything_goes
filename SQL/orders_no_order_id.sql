select
    c.company_name,
    o.order_id
from
    customers c
    LEFT OUTER JOIN orders o On c.customer_id = o.customer_id
where
    o.order_id is null