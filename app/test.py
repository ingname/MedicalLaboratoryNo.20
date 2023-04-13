import psycopg2 as ps

conn = False

try:
    conn = ps.connect(user="postgres",
                      password="7393",
                      host="localhost",
                      port="5432",
                      database="banan")
except:
    exit(print('Че то не робит'))

cursor = conn.cursor()
cursor.execute('SELECT * FROM bananas')
all_users = cursor.fetchall()
print(all_users)

cursor.close()
conn.close()

