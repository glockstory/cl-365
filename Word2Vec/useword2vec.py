from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2VecModel
from pyspark.sql import DataFrame

MODEL_PATH = "model"

spark = SparkSession \
    .builder \
    .appName("word2vec") \
    .getOrCreate()

model = Word2VecModel.load(MODEL_PATH)
count = 20

try:
    word = 'волгоград'

    model.findSynonyms(word, count).show(n=count)
except Exception as ex:
    print("[ERROR] Данного слова нет в словаре!")

spark.stop()