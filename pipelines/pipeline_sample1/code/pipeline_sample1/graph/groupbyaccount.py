from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_sample1.config.ConfigStore import *
from pipeline_sample1.functions import *

def groupbyaccount(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("AccountId"))

    return df1.agg(
        count(lit(1)).alias("No.of opportunities"), 
        sum(col("Amount")).alias("Amount"), 
        sum(col("ExpectedRevenue")).alias("Expected revenue"), 
        max(col("CloseQtr")).alias("last_quarter")
    )
