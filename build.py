import o

def doTheStartInput():
  try:
    print1 = print('Do you want to start dortware?')
    print2 = print('Please reply with either:')
    print3 = print('Yes')
    print4 = print('or')
    print5 = print('No')
    print6andInput = input(">" + ' ')
    try:
      if print6andInput == 'Yes':
        os.system('java -jar dortware.jar')
      elif print6andInput == 'No':
        print('False work!')
      else:
        print("False work!")
  except Exceptiion as givenExceptiononErrorWhenPriningStuffLikePrint2Print2Print3Print4AndPrint5:
    print('Encountered error, contanct devloper for heIp.')

try:
  doTheStartInput()
except Exception as FailedtoDodoTheStartInput:
  print('Erorr' + ' ' + "contact" + ' ' + "drot" + ' ' + "to" + 'fix')

