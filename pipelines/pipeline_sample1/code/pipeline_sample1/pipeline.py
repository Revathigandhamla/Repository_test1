from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline_sample1.config.ConfigStore import *
from pipeline_sample1.functions import *
from prophecy.utils import *
from pipeline_sample1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_salesforce_Account = salesforce_Account(spark)
    df_salesforce_Opportunity = salesforce_Opportunity(spark)
    df_selectfields = selectfields(spark, df_salesforce_Opportunity)
    df_groupbyaccount = groupbyaccount(spark, df_selectfields)
    df_account_opportunity_join = account_opportunity_join(spark, df_salesforce_Account, df_groupbyaccount)
    accounts_delta_tb(spark, df_account_opportunity_join)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("pipeline_sample1").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline_sample1")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline_sample1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
