# %%
import duckdb
import polars as pl
import pandas as pd

# %%
cursor = duckdb.connect()
print(cursor.execute('SELECT 42').fetchall())

# %%
duckdb.sql("SELECT 42").show()

# %%
duckdb.read_csv("data/data_science_salaries.csv")

# %%
duckdb.sql("SELECT * FROM 'data/data_science_salaries.csv'")

# %%
# create a connection to a file called 'file.db'
con = duckdb.connect("data/db_ds_salaries.db")

# %%
con.sql("SHOW TABLES;")

# %%
con.sql("DESCRIBE TABLE tbl_ds_salaries;")

# %%
# create a table and load data into it
#con.sql("CREATE TABLE tbl_ds_salaries AS SELECT * FROM 'data/data_science_salaries.csv'")

# %%
con.table("tbl_ds_salaries").show()

# %%
con.sql("""
    SELECT * FROM tbl_ds_salaries WHERE company_location = 'Germany' """
).show()

# %%
df_arrow = con.query("""
    SELECT * FROM tbl_ds_salaries WHERE company_location = 'Germany' """
).arrow()

# %%
print(df_arrow)

# %%
print(type(df_arrow))

# %%
df_pd = df_arrow.to_pandas()

# %%
df_pd

# %%



