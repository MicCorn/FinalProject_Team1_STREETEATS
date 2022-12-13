import CUSTOMER
##from CUSTOMER import ccNum

#readFile = readline()

def CCisValid(ccNum):
  file = open('creditcards.txt', 'r+')

  new = file.readlines()
  for i in range(len(new)):
    if str(ccNum) in new[i]:
      file.close()
      return True
  file.close()
  return False

def addCC(ccNum):
  file = open('creditcards.txt', 'r+')
  
  result = CCisValid(ccNum)
  if result == False:
    file.write('\n' + str(ccNum))
  file.close()


                  
  

  

  
  