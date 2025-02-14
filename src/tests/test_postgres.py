import psycopg2

conn  = psycopg2.connect(database="fingertipsdb",
                       host="localhost",
                        user="postgres",
                        password="admin123",
                        port="5433")

cursor = conn.cursor()
cursor.execute("select * from news_source")
print(cursor.fetchone())

