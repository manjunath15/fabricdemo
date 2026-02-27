# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f3e38ef5-41d8-4ec4-880d-c49a5d827bbc",
# META       "default_lakehouse_name": "Auto",
# META       "default_lakehouse_workspace_id": "d390287d-9b9b-49de-b411-94cefab25f5e",
# META       "known_lakehouses": [
# META         {
# META           "id": "f3e38ef5-41d8-4ec4-880d-c49a5d827bbc"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

%pip install dbldatagen
%pip install jmespath 

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# This notebook will create 1 Billion records for demo and learning purpose
# we will use Databricks Labs Data Generator library, https://databrickslabs.github.io/dbldatagen/public_docs/index.html
# The Databricks Labs Data Generator project provides a convenient way to generate large volumes of synthetic data 
# from within a Fabric notebook (Originally used for Databricks Notebook).

import dbldatagen as dg
from pyspark.sql.types import StructType, StructField,  StringType
 
spark.sql("""Create table if not exists vehicles(
                name string,
                serial_number string,
                license_plate string,
                email string
                ) using Delta""")
 


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

table_schema = spark.table("vehicles").schema
 
print(table_schema)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

dataspec = (dg.DataGenerator(spark, rows=1000000000)
            .withSchema(table_schema))
 
dataspec = (
    dataspec.withColumnSpec("name", percentNulls=0.01, template=r"\\w \\w|\\w a. \\w")
    .withColumnSpec(
        "serial_number", minValue=1000000, maxValue=2000000000, prefix="dr", random=True
    )
    .withColumnSpec("email", template=r"\\w.\\w@\\w.com")
    .withColumnSpec("license_plate", template=r"\\n-\\n")
)
df1 = dataspec.build()
 
df1.write.format("delta").mode("overwrite").saveAsTable("vehicles")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
