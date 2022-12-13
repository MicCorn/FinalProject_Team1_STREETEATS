  ##Mary

import CUSTOMER
##from CUSTOMER import user_Cart

import time

from random import randint

attempt = 1

#Probability represents probability of rejection
def solicitDelivery(probability, attempts):
  print("looking for driver")
  time.sleep(5)
  x = randint(0,100)
  if x > probability:
    print("Delivery Accepted")
    return attempts
  else:
    print("Delivery Rejected")
    return solicitDelivery(probability - (100 - int(probability/2)), attempts + 1)
  

def returnTime(attempts, distance):
  countdown = distance + 5*attempts
  if countdown < 5:
    raise ValueError("Countdown cannot be less than 5 minutes until delivery")
  return countdown
  #returns a countdown in minutes

  

  
  