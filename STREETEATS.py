import CUSTOMER
from CUSTOMER import CUSTOMER

def create_customer():
  var1 = input("name: ")
  var2 = int(input("Credit Card number: "))
  
  var3 = input("location: ")

  c1 = CUSTOMER(var3, var2, var1)
  c1.Search()

  
  



