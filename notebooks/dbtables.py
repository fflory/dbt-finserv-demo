# Databricks notebook source
display(dbutils.fs.ls("/databricks-datasets/retail-org/customers"))
display(dbutils.fs.ls("/databricks-datasets/retail-org/sales_orders"))

# COMMAND ----------

project_db_input = "felix_flory_dbretail_input"

# COMMAND ----------

spark.sql(f"create schema if not exists {project_db_input}")

# COMMAND ----------

spark.sql(f"DROP TABLE IF EXISTS {project_db_input}.customers_raw")
spark.sql(f"DROP TABLE IF EXISTS {project_db_input}.sales_orders_raw")

# COMMAND ----------

spark.sql(f"""
CREATE TABLE {project_db_input}.customers_raw
USING CSV
OPTIONS (header = "true", inferSchema = "true")
LOCATION '/databricks-datasets/retail-org/customers/'
""")

spark.sql(f"""
CREATE TABLE {project_db_input}.sales_orders_raw
USING JSON
LOCATION '/databricks-datasets/retail-org/sales_orders/'
""")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC show tables in felix_flory_dbretail_input

# COMMAND ----------

# DBTITLE 1,Cleanup
# spark.sql(f"drop schema if exists {project_db_input} cascade")
