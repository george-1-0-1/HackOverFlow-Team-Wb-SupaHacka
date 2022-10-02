import os
os.system("pip install cx.Oracle")
import cx_Oracle

try:
    con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
    print(con.version)
    cursor = con.cursor()
    cursor.execute(
        "create table main(memid integer primary key, name varchar2(30), adhaar integer")
    print("Table Created successfully")
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()