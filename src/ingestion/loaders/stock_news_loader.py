import psycopg2
import os
from dotenv import load_dotenv
class StockNewsLoader:

    def __init__(self):
        load_dotenv()
    def getConn(self):
        return psycopg2.connect(database=os.getenv("PG_DATABASE"),
                                host=os.getenv("PG_HOST"),
                                user=os.getenv("PG_USER"),
                                password=os.getenv("PG_PWD"),
                                port=os.getenv("PG_PORT"))
    def loadTickers(self):
        conn = self.getConn()
        cursor = conn.cursor()
        cursor.execute("select symbol from tickers limit 5")
        results = cursor.fetchall()
        for ticker in results:
            print(ticker[0])

stckNewsLoader = StockNewsLoader()
stckNewsLoader.loadTickers()


        



