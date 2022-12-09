from replit import db

import CUSTOMER
from CUSTOMER import CUSTOMER

import CUSTOMERdb
from CUSTOMERdb import addCustomer
from CUSTOMERdb import returnDB
from CUSTOMERdb import inDB


def logIn():
  var = input("Returning customer? Y/N: ")
  if var.lower() == "y":
    var1 = input("name: ")
    if var1 in db.keys():
      var4 = input("password: ")
      if db[var1][0] == var4:
        print("Welcome")
        var5 = input("location: ")
        c1 = CUSTOMER(var5, db[var1][1], var1)
        c1.Search()
      else:
        logIn()
    else:
      logIn()
  else:
    create_customer()
        
      

def create_customer():
  

  var1 = input("name: ")
  var2 = int(input("Credit Card number: "))
  
  var3 = input("location: ")

  

  c1 = CUSTOMER(var3, var2, var1)

  var4 = input("password: ")

  db[var1] = [var4, var2]

  #addCustomer(c1, var4)
    
    
  

  c1.Search()


 
  #var = input("Returning customer? Y/N: ")
  #if var.lower() == "y":
  #  var1 = input("name: ")
  #  var2 = int(input("Credit Card number: "))
  
   # var3 = input("location: ")

    #c1 = CUSTOMER(var3, var2, var1)
    
    #var4 = input("password: ")
    #addCustomer(c1, var4)
    
    #if inDB(var1, [var4, var2]) == True:
     # pass
    #else:
     # create_customer()

  #else:



  

  
  



