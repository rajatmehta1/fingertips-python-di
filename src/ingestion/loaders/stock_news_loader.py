import psycopg2
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np

class StockNewsLoader:
    def __init__(self):
        load_dotenv()
        self.embedding_finder = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    def getConn(self):
        return psycopg2.connect(database=os.getenv("PG_DATABASE"),
                                host=os.getenv("PG_HOST"),
                                user=os.getenv("PG_USER"),
                                password=os.getenv("PG_PWD"),
                                port=os.getenv("PG_PORT"))
    def loadNews(self):
        conn = self.getConn()
        cursor = conn.cursor()
        cur1 = conn.cursor()
        cursor.execute("select newsid,title,source,content from news limit 5")
        results = cursor.fetchall()
        for news in results:
            sql1 = "update news set news_embedding = ARRAY" + str(list(self.calcEmbedding(news[3]))) + " where newsid=" + str(news[0])
            print(sql1)
            cur1.execute(sql1)
        conn.commit()

    def calcEmbedding(self, input):
        qry_rst = self.embedding_finder.embed_query(input)
        decimal_places = 5
        rounded_embeddings = np.round(qry_rst,decimals=decimal_places)
        # print(qry_rst)
        return rounded_embeddings[:128]

stckNewsLoader = StockNewsLoader()
stckNewsLoader.loadNews()


        



