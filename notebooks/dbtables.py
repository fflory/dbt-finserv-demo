# Databricks notebook source
# %pip install PyYAML

# COMMAND ----------

import yaml
from pathlib import Path

conf = yaml.safe_load(Path('../dbt_project.yml').read_text())
project_db_input = conf.get("vars").get("source_db")
print(project_db_input)

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets/retail-org/customers"))
display(dbutils.fs.ls("/databricks-datasets/retail-org/sales_orders"))

# COMMAND ----------

spark.sql(f"create schema if not exists {project_db_input}")

# COMMAND ----------

spark.sql(f"DROP TABLE IF EXISTS {project_db_input}.customers_raw")
spark.sql(f"DROP TABLE IF EXISTS {project_db_input}.sales_orders_raw")

# COMMAND ----------

(spark.read.format("csv").option("header", "true")
 .load("/databricks-datasets/retail-org/customers")
 .write.mode("overwrite")
 .saveAsTable(name = "uc_demos_felix_flory.felix_flory_dbt_finserv_demo.customers_raw")
)

(spark.read.format("json")
 .load("/databricks-datasets/retail-org/sales_orders/")
 .write.mode("overwrite")
 .saveAsTable(name = "uc_demos_felix_flory.felix_flory_dbt_finserv_demo.sales_orders_raw")
)

# COMMAND ----------

display(spark.sql("select * from uc_demos_felix_flory.felix_flory_dbt_finserv_demo.sales_orders_raw where order_datetime is null"))

# COMMAND ----------

# spark.sql(f"""
# CREATE TABLE {project_db_input}.customers_raw
# USING CSV
# OPTIONS (header = "true", inferSchema = "true")
# LOCATION '/databricks-datasets/retail-org/customers/'
# """)

# spark.sql(f"""
# CREATE TABLE {project_db_input}.sales_orders_raw
# USING JSON
# LOCATION '/databricks-datasets/retail-org/sales_orders/'
# """)

# COMMAND ----------

# DBTITLE 1,Cleanup dbt
spark.sql(f"DROP VIEW IF EXISTS {project_db_input}.customers")
spark.sql(f"DROP VIEW IF EXISTS {project_db_input}.sales_orders")
spark.sql(f"DROP VIEW IF EXISTS {project_db_input}.sales_orders_cleaned")
spark.sql(f"DROP VIEW IF EXISTS {project_db_input}.sales_order_in_chicago")
spark.sql(f"DROP VIEW IF EXISTS {project_db_input}.sales_order_in_la")

# spark.sql(f"DROP TABLE IF EXISTS {project_db_input}.imid_confict_list")
# spark.sql(f"drop schema if exists {project_db_input} cascade")

# COMMAND ----------

dlt_target_schema = "felix_flory_dbt_finserv_demo"

# COMMAND ----------

# DBTITLE 1,Cleanup dlt
spark.sql(f"DROP TABLE IF EXISTS {dlt_target_schema}.customers")
spark.sql(f"DROP TABLE IF EXISTS {dlt_target_schema}.sales_orders_raw")
spark.sql(f"DROP TABLE IF EXISTS {dlt_target_schema}.sales_orders_cleaned")
spark.sql(f"DROP TABLE IF EXISTS {dlt_target_schema}.sales_order_in_chicago")
spark.sql(f"DROP TABLE IF EXISTS {dlt_target_schema}.sales_order_in_la")

# spark.sql(f"drop schema if exists {dlt_target_schema} cascade")
