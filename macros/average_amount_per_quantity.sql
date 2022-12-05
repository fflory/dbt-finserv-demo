{% macro average_amount_per_quantity() %}
    (sales / quantity) ::numeric(16, 2)
{% endmacro %}
