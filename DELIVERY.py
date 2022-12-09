##Mary

import CUSTOMER
from CUSTOMER import user_Cart

import time

def solicitDelivery(user_Cart):
  global seconds
  seconds = 0
  return True


def returnTime(seconds):
  seconds = seconds + 5
  time.sleep(seconds)

  

  
  