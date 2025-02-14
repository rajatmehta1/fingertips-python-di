import os

import pandas as pd
from dotenv import load_dotenv
import psycopg2
import pandas
class SP500TickersIngester:

    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    def __init__(self):
        load_dotenv()
        self.conn = psycopg2.connect(database=os.getenv("PG_DATABASE"),
                                     host=os.getenv("PG_HOST"),
                                     user=os.getenv("PG_USER"),
                                     password=os.getenv("PG_PWD"),
                                     port=os.getenv("PG_PORT"))

    def loadFromWikipedia(self):
        tables = pd.read_html(SP500TickersIngester.wiki_url)
        sp500_table = tables[0]
        df = sp500_table[['Symbol','Security','GICS Sector','GICS Sub-Industry']].values.tolist()
        return df

    def ingestSP500TickersFromWikipedia(self):
        df = self.loadFromWikipedia()
        cursor = self.conn.cursor()
        cursor.execute("delete from tickers")
        for rst in df:
            symbol = rst[0]
            name = rst[1].replace("'","''")
            category = rst[2].replace("'","''")
            sector = rst[3].replace("'","''")
            print(f"insert into tickers(symbol,companyname,sector,industry) values('{symbol}','{name}','{category}','{sector}')")
            print(cursor.execute(f"insert into tickers(symbol,companyname,sector,industry) values('{symbol}','{name}','{category}','{sector}')"))
        self.conn.commit()
        cursor.close()

        # def insert_vendor(vendor_name):
        #     """ Insert a new vendor into the vendors table """
        #     sql = """INSERT INTO vendors(vendor_name)
        #              VALUES(%s) RETURNING vendor_id;"""
        #     vendor_id = None
        #     config = load_config()
        #     try:
        #         with  psycopg2.connect(**config) as conn:
        #             with  conn.cursor() as cur:
        #                 # execute the INSERT statement
        #                 cur.execute(sql, (vendor_name,))
        #                 # get the generated id back
        #                 rows = cur.fetchone()
        #                 if rows:
        #                     vendor_id = rows[0]
        #                 # commit the changes to the database
        #                 conn.commit()
        #     except (Exception, psycopg2.DatabaseError) as error:
        #         print(error)
        #     finally:
        #         return vendor_id

r = SP500TickersIngester()
r.ingestSP500TickersFromWikipedia()

