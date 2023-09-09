import mysql.connector
mydb=mysql.connector.connect(
 host="localhost",
 user="chandru",
 password="********",
 database="covid_19",
)
mycursor=mydb.cursor()
#********************************************#
# mycursor.execute("create database covid_19")
# print("successfully database created")
# mycursor.execute("create table coviddatas(DISTRICTNAME varchar(100),TOTALPOPLE
# int,NEWCASES int,DEATHCASES int,ACTIVECASES int,TOTALCASES int)")
# print("successfully table created")
# def insert_studentdata():
import datetime
from datetime import date
x=datetime.datetime.now()
today=x.strftime("%A")
print(today)
this_month=x.strftime("%B")
print(this_month)
this_year=x.strftime("%Y")
print(this_year)
current_time=int(x.strftime("%H"))
# print(current_time)
current_minitue=x.strftime("%M")
# print(current_minitue)
print(f"{current_time}:{current_minitue}")
date=date.today()
print(date)
def insert_coviddatas():
    sql="insert into coviddatas(DISTRICTNAME,TOTALPOPLE,NEWCASES,DEATHCASES,ACTIVECASES,TOTALCASES)values (%s,%s,%s,%s,%s,%s)"
    DISTRICTNAME=input("enter your name DISTRICTNAME:")
    TOTALPOPLE=int(input("TOTALPOPLE:"))
    NEWCASES=int(input("NEWCASES:"))
    DEATHCASES=int(input("DEATHCASES:"))
    ACTIVECASES=int(input("ACTIVECASES:"))
    TOTALCASES=(NEWCASES+DEATHCASES+ACTIVECASES)
    # print(TOTALCASES,"TOTALCASES")
    val=(DISTRICTNAME,TOTALPOPLE,NEWCASES,DEATHCASES,ACTIVECASES,TOTALCASES)
    mycursor.execute(sql,val)
    mydb.commit()
    print("table created successfully")
def view_coviddatas():
    mycursor.execute("select * from coviddatas")
    result=mycursor.fetchall()
    for i in result:
        print(i)
def update_coviddatas():
    sql="update from coviddatas address where address"
    address=input("enter your update address")
    val=(address)
    print("data update succwssfully")
def delete_covidtatas():
    sql="delete from coviddatas where address"
    address=input("enter")
    val=(address)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data deleted succwssfully")
def exit_coviddatas():
     print(exit)
while True:
    print("-->1.insert data")
    print("-->2.view data")
    print("-->3.update data")
    print("-->4.delete data")
    print("-->5.exit data")
user=int(input("enter your choice:"))
if user==1:
    insert_coviddatas()
elif user==2:
     view_coviddatas()
elif user==3:
    update_coviddatas()
elif user==4:
    delete_covidtatas()
elif user==5:
    exit_coviddatas()
else:
    print("please type 1 to 5")
# else:
#  print(exit())