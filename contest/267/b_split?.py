S = str(input())
pin = [False for _ in range(10)]

for i in range(len(S)):
  if int(S[i]) == 0:
    pin[i] = True

while True:
  if pin[0] == False:
    print('No')
    break

  if pin[4] == False:
    if pin[5] == False and pin[2] == True and pin[8] == True:
      print('Yes')
      break
    if pin[9] == False and pin[5] == True and pin[2] == True and pin[8] == True:
      print('Yes')
      break
    if pin[3] == False and pin[1] == True and pin[7] == True:
      print('Yes')
      break
    if pin[6] == False and pin[3] == True and pin[1] == True and pin[7] == True:
      print('Yes')
      break

  if pin[4] == True:
    if pin[1] == False or pin[7] == False:
      if pin[2] == False or pin[8] == False:
        print('Yes')
        break
      if pin[5] == False and pin[2] == True and pin[8] == True:
        print('Yes')
        break
      if pin[9] == False and pin[5] == True and pin[2] == True and pin[8] == True:
        print('Yes')
        break
    if pin[3] == False:
      if pin[1] == True and pin[7] == True:
        if pin[2] == False or pin[8] == False:
          print('Yes')
          break
        if pin[2] == True and pin[8] == True and pin[5] == False:
          print('Yes')
          break
        if pin[9] == False and pin[2] == True and pin[8] == True and pin[5] == True:
          print('Yes')
          break
    if pin[6] == False:
      if (pin[1] == False or pin[7] == False) and pin[3] == True:
        print('Yes')
        break
      if pin[3] == True and pin[3] == True and pin[7] == True:
        if pin[2] == False or pin[8] == False:
          print('Yes')
          break
        if pin[2] == True and pin[8] == True:
          if pin [5] == False:
            print('Yes')
            break
          if pin[5] == True and pin[9] == False:
            print('Yes')
            break
  print('No')
  break
