import mysql.connector


con = mysql.connector.connect(host='localhost',user='root',password='ezrengel',database='kyc')
cur = con.cursor()

from mysql.connector import errorcode
import pickle

def createtable1(): #maintable
    global con,cur
    cur.execute("CREATE TABLE book(tid integer PRIMARY KEY,name varchar(25), gmail varchar(50),doj date);")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)
        
#createtable1()

def createtable2a(): #main details
    global con,cur
    cur.execute("CREATE TABLE deetsa(did integer, name varchar(25), dob date, gender varchar(10), adhaar int, pan varchar(10), gmail varchar(50), mobile integer );")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)

def createtable2b(): #secondary details
    global con,cur
    cur.execute("CREATE TABLE deetsb(did integer, minor varchar(10), marital varchar(10), spousenm varchar(10), religion varchar(15) , category varchar(10), occupation varchar(20), income integer );")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)


def createtable2c(): #adress
    global con,cur
    cur.execute("CREATE TABLE deetsc(did integer, hnonm varchar(20), vill varchar(20), post char(20), dist varchar(20), pin integer, state varchar(15), country varchar(20));")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)

def createtable3a(): #login
    global con,cur
    cur.execute("CREATE TABLE user(tid integer PRIMARY KEY,pass varchar(20));")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)


def createtable3b(): #login status
    global con,cur
    cur.execute("CREATE TABLE userstatus(id int,tid integer PRIMARY KEY,status varchar(10));")
    con.commit()
    cur.execute('show tables')
    for x in cur:
        print(x)


#createtable2a()
#createtable2b()
#createtable2c()
#createtable3a()
#createtable3b()

def saveall1(): #save from main table
    global con,cur
    try:
        query ="select * from book"
        cur.execute(query)
        results=cur.fetchall()
        f=open('book.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')

def saveall2a(): #save from main details
    global con,cur
    try:
        query ="select * from deetsa"
        cur.execute(query)
        results=cur.fetchall()
        f=open('deetsa.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')

def saveall2b(): #save from secondary details
    global con,cur
    try:
        query ="select * from deetsb"
        cur.execute(query)
        results=cur.fetchall()
        f=open('deetsb.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')

def saveall2c(): #same from address
    global con,cur
    try:
        query ="select * from deetsc"
        cur.execute(query)
        results=cur.fetchall()
        f=open('deetsc.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')
    
def saveall3a(): #save from user
    global con,cur
    try:
        query ="select * from user"
        cur.execute(query)
        results=cur.fetchall()
        f=open('user.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')

def saveall3b(): #save from user status
    global con,cur
    try:
        query ="select * from userstatus"
        cur.execute(query)
        results=cur.fetchall()
        f=open('userstatus.dat','wb')
        pickle.dump(results,f)
        f.close()
               
    except ValueError:
        print('Unable to add data because of incorrect data type ')

saveall1()
def addbook(): #add deets to book
    c=1000
    f=open('book.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        tid=c
        name=input()
        gmail=input()
        query="select CURDATE()"
        cur.execute(query)
        m=cur.fetchone()
        doj=m[0]
        query="insert into book values(%s,%s,%s,%s);"
        data=(str(tid),name,gmail,doj)
        cur.execute(query,data)
        con.commit()
        saveall1()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')


#addbook()
saveall2a()
def adddeets2a(): #add deets to main detals

    c=1000
    f=open('deetsa.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        did=c
        name=input()
        gender=input()
        adhaar=int(input())
        pan=input()
        gmail=input()
        mobile=int(input())
        query="select CURDATE()"
        cur.execute(query)
        m=cur.fetchone()
        dob=m[0]
        query="insert into deetsa values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(str(did),name,dob,gender,str(adhaar),pan,gmail,mobile)
        cur.execute(query,data)
        con.commit()
        saveall2b()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('WRONG DATABASE ',err)
        elif err.errno==errorcode.ER_BAD_TABLE_ERROR:
            print('WRONG TABLE')
        else:
            print('SOME OTHER ERROR ',err)

#adddeets2a()

def adddeets2b(): #add deets to secondary deets
    saveall2b()
    c=1000
    f=open('deetsb.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        did=c
        minor=input()
        marital=input()
        spousenm=input()
        religion=input()
        category=input()
        occupation=input()
        income=int(input())
        query="insert into deetsb values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(str(did),minor,marital,spousenm,religion,category,occupation,str(income))
        cur.execute(query,data)
        con.commit()
        saveall2b()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('WRONG DATABASE ',err)
        elif err.errno==errorcode.ER_BAD_TABLE_ERROR:
            print('WRONG TABLE')
        else:
            print('SOME OTHER ERROR ',err)

#adddeets2b()

def adddeets2c(): #add deets to address
    saveall2c()
    c=1000
    f=open('deetsc.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        did=c
        hnonm=input()
        vill=input()
        post=input()
        dist=input()
        pin=int(input())
        state=input()
        country=input()
        query="insert into deetsc values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(str(did),hnonm,vill,post,dist,str(pin),state,country)
        cur.execute(query,data)
        con.commit()
        saveall2c()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print('WRONG DATABASE ',err)
        elif err.errno==errorcode.ER_BAD_TABLE_ERROR:
            print('WRONG TABLE')
        else:
            print('SOME OTHER ERROR ',err)

#adddeets2c()

def adduser(): #add user login
    saveall3a()
    c=1000
    f=open('user.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        did=c
        pasw = input()
        query="insert into user values(%s,%s)"
        data=(str(did),pasw)
        cur.execute(query,data)
        con.commit()
        saveall3a()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')

adduser()

def adduser(): #to keep login status
    saveall3a()
    c=1000
    f=open('user.dat','rb')
    rec=pickle.load(f)
    for row in rec:
        c+=1 
    f.close()
    global con,cur
    try:
        did=c
        pasw = input()
        query="insert into user values(%s,%s)"
        data=(str(did),pasw)
        cur.execute(query,data)
        con.commit()
        saveall3a()
        
    except ValueError:
        print('Unable to add data because of incorrect data type ')

#adduser()

