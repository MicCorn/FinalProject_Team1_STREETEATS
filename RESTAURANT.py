##Jiean

import CUSTOMER
#from CUSTOMER import user_Cart

from random import randint


## returns the digital menu of the restaurant, includes promotions
def menu(restaurant, price_level):
  menuDic = {'pita kebab': 3.5, 'durum kebab' : 4, 'chicken briyani' : 7, 'menu pita' : 7, 'adana grill' : 12, 'manti' : 8, 'ULTRA MEGA SMASH KEBAB' : 169, 'VIP FORTNITE KEBAB' : 55
    
  }
  if price_level == None:
    price_level = 2

  for x in menuDic.keys():
    menuDic.update({x : menuDic[x] * price_level})
  
  return menuDic


def promotions(cart):
  num = 0
  for i in cart:
	  if i in d:
		  d[i] = d[i] + 1
	  else:
		  d[i] = 1
      
  #List of lists
  #Buy 1 get 1 Free, Spend 10 save 7, Buy 2 get 1 Free, 
  #iterates through the User's Carts, checks for promotions, adds to num
  return num


def solicitOrder(user_Cart, price):
  x = randint(0, 100)

  if x <= 95:
    var = True
  else:
    var = False
  ##random variable that accepts/rejects order
  return var
  
  
  