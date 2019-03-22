import os
import sqlite3

def add_student(name='',regdNo=''):
    #name=input("Enter Student's Name: ")
    #regdNo=input("Enter Student's Roll Number: ")

    print('name=',name)
    print('regd=',regdNo)
    print('I m in add_student')
    #Inserting Name and Regd No. Into Database
    
    

    try:
        print('try First line')
        conn=sqlite3.connect("test.db")
        curr=conn.cursor()
        curr.execute("CREATE TABLE IF NOT EXISTS CSED (REGDNO INTEGER PRIMARY KEY,NAME VARCHAR2)")

        curr.execute("INSERT INTO CSED VALUES(?,?)",(regdNo,name))

        '''
        curr.execute("SELECT * FROM CSED")
        al=curr.fetchall()

        print(al)
        for row in al:
            print(row)
        '''
        conn.commit()
        conn.close()

        print('I m in try block')

        folderPathImages='Images/'+regdNo
        folderPathPkl='Pkl/'+regdNo

        if not os.path.exists(folderPathImages):
            os.makedirs(folderPathImages)
            os.makedirs(folderPathPkl)
    except sqlite3.IntegrityError:
        pass