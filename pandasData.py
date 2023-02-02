# import pandas as pd
# import numpy as np
# from pandasql import sqldf


# data = pd.read_csv("./chatlogs/uncleanData.csv")
# query = "SELECT user FROM data;"
# print(data.head())

from pandasql import sqldf, load_meat, load_births
def pysqldf(q): return sqldf(q, globals())


meat = load_meat()
births = load_births()
print(pysqldf("SELECT * FROM meat LIMIT 10;").head())
