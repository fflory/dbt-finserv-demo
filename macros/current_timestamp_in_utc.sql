{% macro spark__current_timestamp_in_utc() %}
    convert_timezone('UTC', {{dbt_utils.current_timestamp()}})::{{type_timestamp()}}
{% endmacro %}

{% macro databricks__current_timestamp_in_utc() %}
    {{spark__current_timestamp_in_utc()}}
{% endmacro %}
