select
  f.customer_id, f.customer_name, f.number_of_line_items, 
  timestamp(from_unixtime((cast(case when f.order_datetime = "" then null else f.order_datetime end as long)))) as order_datetime, 
  date(from_unixtime((cast(case when f.order_datetime = "" then null else f.order_datetime end as long)))) as order_date, 
  f.order_number, f.ordered_products, c.state, c.city, c.lon, c.lat,
  c.units_purchased, c.loyalty_segment
FROM {{ ref('sales_orders') }} f
LEFT JOIN {{ ref('customers') }} c
  ON c.customer_id = f.customer_id
  AND c.customer_name = f.customer_name
