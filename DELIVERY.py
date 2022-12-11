##Mary

import CUSTOMER
##from CUSTOMER import user_Cart

import time

from random import randint

attempt = 1

def solicitDelivery(probability, attempts):
  print("looking for driver")
  time.sleep(5)
  x = randint(0,100)
  if x > probability:
    print("Delivery Accepted")
    return attempts
  else:
    print("Delivery Rejected")
    solicitDelivery(probability - (100 - int(probability/2)), attempts + 1)
  

def returnTime(attempts, distance):
  
  countdown = distance + 5*attempts
  pass
  #returns a countdown in minutes

  

  
  