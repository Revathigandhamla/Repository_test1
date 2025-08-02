from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_sample1.config.ConfigStore import *
from pipeline_sample1.functions import *

def selectfields(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(year(to_date(col("CloseDate"))), lit("Q"), quarter(col("CloseDate"))).alias("CloseQtr"), 
        col("AccountId"), 
        col("Amount"), 
        col("ExpectedRevenue")
    )
