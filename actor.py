import csv
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='ruskin123bond',database='ACTOR_TRAITS')
print('databse connected')
cursor=mydb.cursor()
csv_data=csv.reader(open('traits.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO USER1 (ACTOR,TRAITS) VALUES (%s,%s)',row)
    print(row)
mydb.commit()
cursor.close()
print('done')


