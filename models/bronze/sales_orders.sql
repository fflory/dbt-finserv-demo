select
  clicked_items,
  customer_id,
  customer_name,
  number_of_line_items,
  order_datetime,
  order_number,
  ordered_products,
  promo_info
from {{ var('source_db') }}.sales_orders_raw
-- from json.`/databricks-datasets/retail-org/sales_orders/`
