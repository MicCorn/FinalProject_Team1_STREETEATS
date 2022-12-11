import LOCATION
from LOCATION import search

import RESTAURANT
from RESTAURANT import menu
from RESTAURANT import promotions
from RESTAURANT import solicitOrder

import CREDITCARD
from CREDITCARD import CCisValid

import DELIVERY
from DELIVERY import solicitDelivery
from DELIVERY import returnTime


class CUSTOMER():

  global user_Cart 
  user_Cart = []
  
  def __init__(self, location, ccNum, name):
    self.__a = location
    self.__b = ccNum
    self.__c = name


  def getDistance(self, foodDic):
    pass

  def Search(self):
    user_Cart = []
    
    foodDic = search(self.__a)
    list = []
    for x in foodDic:
      print(x, ": ")
      for y in foodDic[x]:
        list.append(foodDic[x][y])
      print("   " , list)
      list = []
    
    print("Cart: ", user_Cart)
    self.findFood(foodDic)

    
  
  def findFood(self, foodDic):
    x = True
    while x is True:
      selection = input("Please select a restaurant (E to break): ")
      
      if selection.lower() == 'e':
        print("... exiting")
        break
      else:
        menuDic = self.getMenu(selection, foodDic)
        if menuDic != False:
          print(menuDic)
          var = input("Would you like to order here? Y/N: ")
          if var == "Y":
            x = False
            self.order(selection, menuDic, foodDic)
          else:
            x = False
            self.findFood(foodDic)
        else:
          x = False
          self.findFood(foodDic)     

      
        
  def getMenu(self, selection, foodDic):
    if selection.lower() in foodDic.keys():
      return menu(selection)
    else:
      return False
      
    
  
  def order(self, selection, menuDic, foodDic):

    x = True
    while x is True:
      var = input("Add an item to your cart: \nIf you want to exit return NO: \nIf you want to check out return CHECKOUT: ")
      if var.lower() == 'no':
        print(user_Cart)
        self.findFood(foodDic)

      elif var.lower() == 'checkout':
        x = False
        print(user_Cart)
        self.checkOut(foodDic)
        
      elif var.lower() in menuDic.keys():
        self.addItem(var.lower(), menuDic[var])

 
  def addItem(self, item, price):
    user_Cart.append([item, price])
    print(item + " has been added to your cart")
    print(user_Cart)

  
  
  def removeItem(self, item, num):
    for x in user_Cart:
      if x[0] == item:
        print(user_Cart.pop(x) + 'has been removed from your cart')



  def checkOut(self, foodDic):
    totalprice = 0
    discount = promotions(user_Cart)
    for x in user_Cart:
      print(x)
      totalprice += int(x[1])

    if discount != 0:
      print("Congratulations! Your subtotal of " + str(totalprice) + "has been reduced to " + str(totalprice - discount))
    else:
      print("You have a pending subtotal of " + str(totalprice))

    
    if CCisValid(self.__b):
      if solicitOrder(user_Cart, totalprice - discount) is True:
        pud = input("Pick up or delivery? pu/d: ")
        if pud == 'd':
          #if solicitDelivery(user_Cart) is True:
          attempts = solicitDelivery(50, 1)
          print("Your food is on the way " + self.__c + "!")
          #countdown
          #need help getting the distance, foodDIc is passed in the method (the one that spits everything), put distance as 0 for now
          print(returnTime(attempts, 0))
            
        else:
          print("Your food will be ready for pick up soon!")


  def contact(self):
    pass

##All the getter methods, these are not for customer themself to use, but for the KEBAB OCLOCK team to access user information.

  def getName(self):
    return self.__c

  def getLocation(self):
    return self.__a

  def getccNum(self):
    return self.__b

class RegisteredUser(CUSTOMER):
  def __init__(self, location, ccNum, name):
      super().__init__(location, ccNum, name)

  
  
  