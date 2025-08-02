from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_sample1.config.ConfigStore import *
from pipeline_sample1.functions import *

def accounts_delta_tb(spark: SparkSession, in0: DataFrame):
    in0.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`hive_metastore`.`default`.`accounts_delta_tb2`")
