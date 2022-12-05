conda create --name dbt -c conda-forge \
  python=3.9.13 \
  dbt-core \
  databricks-cli \
  databricks-sql-connector
conda activate dbt
python -m pip install dbt-databricks
