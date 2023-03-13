import pyterrier as pt
import pandas as pd

if not pt.started():
    pt.init()


indexref = pt.IndexFactory.of("./index/data.properties")
tfidf = pt.BatchRetrieve(indexref, wmodel="TF_IDF")

queries = ["cork city", "aerlingus", "ireland", "india"]

for query in queries:
    result = tfidf.search(query)
    print(result)
