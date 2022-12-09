##Mary

import CUSTOMER
from CUSTOMER import user_Cart

import time

from random import randint

attempt = 1

def solicitDelivery(attempt):
  time.sleep(5)
  limit = int(50/attempt)
  x = randint(0,100)
  if x > 50:
    #returnTime(attempt)
    #print(x)
    #print(attempt)
    print("Delivery Accepted")
    return attempt
  if x <= 50:
    print(x)
    print("Delivery Rejected")
    attempt = attempt + 1
    solicitDelivery(attempt)

def returnTime(attempts):
  attempt = solicitDelivery(1)
  countdown = countdown + 5*attempt
  return countdown

  

  
  