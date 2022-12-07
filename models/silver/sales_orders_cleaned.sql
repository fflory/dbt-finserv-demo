select
  f.customer_id, f.customer_name, f.number_of_line_items, 
  -- -- timestamp(from_unixtime((cast(f.order_datetime as long)))) as order_datetime, 
  to_timestamp(f.order_datetime) as order_datetime, 
  -- date(from_unixtime((cast(f.order_datetime as long)))) as order_date, 
  to_date(to_timestamp(f.order_datetime)) as order_date,
  f.order_number, f.ordered_products, c.state, c.city, c.lon, c.lat,
  c.units_purchased, c.loyalty_segment
FROM {{ ref('sales_orders') }} f
LEFT JOIN {{ ref('customers') }} c
  ON c.customer_id = f.customer_id
  AND c.customer_name = f.customer_name
-- where f.order_datetime is not null
