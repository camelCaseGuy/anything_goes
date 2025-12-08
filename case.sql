select DISTINCT
    country,
    case
        WHEN country = 'USA' THEN 'Local'
        WHEN country = 'Canada' THEN 'Semi-Local'
        WHEN country = 'Mexico' THEN 'Semi-Local'
        ELSE 'Foreign'
    END AS 'shipping_rate'
from
    customers
WHERE
    country is not null
order by
    country