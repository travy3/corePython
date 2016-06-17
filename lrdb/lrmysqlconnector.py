import pymysql

conn = pymysql.connect(host='localhost', user='root', password="123", db='test')

cursor =conn.cursor()

cursor.execute('insert into vahr(id,name) VALUES(%d, %s)', [1, '阿斯顿'])

print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()

cursor.execute('select * from vahr WHERE  IDENTITY = %d', ('1',))

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

