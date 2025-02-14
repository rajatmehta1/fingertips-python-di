import psycopg2

class PostgresDao:

    def __init__(self):
        self.conn  = psycopg2.connect(database="fingertipsdb", host="localhost", user="postgres", password="admin123", port="5433")
        self.cursor = self.conn.cursor()

    def drop_insert_sp500(self,stck_lst):
        self.cursor.execute("delete from stock_symbols")
        for stck in stck_lst:
            self.cursor.execute("insert into stock_symbols values('%s','%s','%s','%s','%s')" % (stck,stck,stck,'Y','Y'))
            self.conn.commit()

