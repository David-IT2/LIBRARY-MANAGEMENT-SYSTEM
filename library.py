import mysql. connector as a
#In the password sector in the connect function place your database's password and it leave empty in case you didn't set one
con=a.connect (host=" localhost", user=" root", password="mysql", database="Library")
#Returns 'True' if there is a connection
print(con.is_connected())
c=con.cursor()

def addmember():
 bn=input("enter the member name : ")
 c=input ( "enter the member regno : ")
 data=(bn,c)
 sql='insert into members values(%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("============")
 print("MEMBER ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 

def updatememb():
 ac=input("enter  member regno:")
 bc=input("enter member name:")
 a="UPDATE members SET NAME=%s WHERE REGNO=%s"
 data=(bc,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print (c.rowcount)
 print("MEMBER UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 

def deletememb():
 c=input ( "enter the member regno : ")
 data=(c,)
 sql="delete from members where regno=%s"
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("MEMBER DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")


def dispmemb():
 a="select * from members"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No members available....ADD MEMBER")
 else:
     print("Members available:")
 for i in myresult:
     print("Member name : ",i[0])
     print("Member regno : ",i[1])
     print ("============= ")
     anykey=input("Press and Enter anykey to return to menu:")
     




def addpub():
 bn=input("enter the publication name : ")
 c=input ( "enter the publication code : ")
 t=input( "total book : ")
 s=input("enter subject : ")
 data=(bn,c, t, s)
 sql='insert into books values(%s,%s,%s,%s)'
 c=con. cursor()
 c. execute( sql,data)
 con.commit()
 print (" =============")
 print("BOOK ADDED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 


def issued():
 n=input ( "enter loaner name : ")
 r=input("enter the reg no:")
 co=input ( "enter book code:")
 d=input("enter date : ")
 a='insert into issue values(%s,%s,%s,%s)'
 data=(n,r,co,d)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("Book Issued To :",n)
 bookup(co, -1)
 anykey=input("Press and Enter anykey to return to menu:")


def dispissue():
 a="select * from issue"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No issue available....ADD ISSUE")
 else:
     print("Issue available:")
 for i in myresult:
     print(" name : ",i[0])
     print("regno : ",i[1])
     print("bcode : ",i[2])
     print("issue date:",i[3])
     print ("============= ")
     anykey=input("Press and Enter anykey to return to menu:")
     

def returnp():
 n=input ( "enter the name : ")
 r=input ( "enter the reg no:")
 co=input("enter book code : ")
 d=input ( "enter date : ")
 a=' insert into submit values(%s,%s,%s,%s)'
 data=(n,r,co,d)
 c=con. cursor()
 c. execute ( a, data)
 con.commit()

 a="delete from issue where regno=%s"
 data=(r,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print (" Book returned by :",n)
 bookup(co,+1)
 anykey=input("Press and Enter anykey to return to menu:")


def bookup(co,u):
 a="select TOTAL from books where BCODE = %s"
 data=(co,)
 c=con. cursor()
 c.execute(a,data)
 myresult=c. fetchone ()
 t=myresult[0] + u
 sql="update books set TOTAL = %s where BCODE =%s"
 d=(t,co)
 c. execute ( sql,d)
 con.commit()
 anykey=input("Press and Enter anykey to return to menu:")
 
def updatepub():
 ac=input("enter  book  code:")
 bc=input("enter book name:")
 a="UPDATE books SET BNAME=%s WHERE BCODE=%s"
 data=(bc,ac)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print (c.rowcount)
 print("PUBLICATION UPDATED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 

def deletepub():
 ac=input("enter  book  code:")
 a="delete from books where BCODE=%s"
 data=(ac,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("BOOK DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 

def dispbook():
 a="select * from books"
 c=con.cursor()
 c.execute(a)
 myresult=c. fetchall ()
 if len(myresult)==0:
     print("No books available...ADD A BOOK ")
 else:
     print("Books available are:")
     for i in myresult:
         print("book name : ",i[0])
         print("book code : ",i[1])
         print("total : ",i[2])
         print("subject:",i[3])
         print ("============= ")
         anykey=input("Press and Enter anykey to return to menu:")
     


def dsubmit():
 ad=input("enter name:")
 a="delete from submit where name=%s"
 data=(ad,)
 c=con. cursor()
 c.execute(a,data)
 con.commit()
 print ("=============")
 print("SUBMISSION DELETED SUCCESSFULLY")
 anykey=input("Press and Enter anykey to return to menu:")
 

def main():    
 print("""

WELCOME TO THE LIBRARY MANAGEMNT SYSTEM

1.ADD PUBLICATION
2.UPDATE PUBLICATION
3.ISSUE PUBLICATION
4.RETURN PUBLICATION
5.DELETE PUBLICATION
6.DISPLAY PUBLICATION
7.ADD MEMBER
8.DELETE MEMBER
9.UPDATE MEMBER
10.DISPLAY MEMBERS
11.DISPLAY ISSUE""")
while True:
        main()
        choice=int(input("Enter  Task No:"))
        if (choice==1):
            addpub()
            
        elif(choice==2):
            updatepub()
            
        elif(choice==3):
            issued()
            
        elif(choice==4):
            returnp()
           
        elif(choice==5):
            deletepub()
            
        elif(choice==6):
            dispbook()
            
        elif(choice==7):
            addmember()
            
        elif(choice==8):
            deletememb()
            
        elif(choice==9):
            updatememb()
            
        elif(choice==10):
            dispmemb()
            
        elif(choice==11):
            dispissue()
            
        else:
            print("Invalid choice.Enter 1-11...")
            
    
               
            
            
           
    
           


        
   
        
            
    
