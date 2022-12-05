with tbl as (
SELECT
  city, order_date, customer_id, customer_name, ordered_products_explode.curr,
  current_timestamp() as cts,
  sum(ordered_products_explode.price) as sales, 
  sum(ordered_products_explode.qty) as quantity, 
  count(ordered_products_explode.id) as product_count
FROM (
  SELECT
    city, order_date, customer_id, customer_name,
    explode(ordered_products) as ordered_products_explode
  FROM {{ ref('sales_orders_cleaned') }}
   WHERE city = 'Chicago')
GROUP BY order_date, city, customer_id, customer_name, ordered_products_explode.curr
)
select *,
  {{ average_amount_per_quantity() }} as average_amount_per_quantity
from tbl
