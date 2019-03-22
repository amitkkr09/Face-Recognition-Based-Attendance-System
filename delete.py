import sqlite3

regdno=int(input('Enter Regd no. to be deleted:'))

conn=sqlite3.connect('test.db')
cur=conn.cursor()
cur.execute('DELETE FROM CSED WHERE REGDNO=?',(regdno,))
conn.commit()
conn.close()