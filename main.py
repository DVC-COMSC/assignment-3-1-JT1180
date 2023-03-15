def main():
    ##################################################
    # Comlete your code here
    ##################################################
  import random
  num1 = random.randint(0,100)
  num2 = random.randint(0,100)
  num3 = random.randint(0,100)

  if (num1 <= num2) and (num1 <= num3):
    smallest = num1
  elif (num2 <= num1) and (num2 <= num3):
     smallest = num2
  else:
    smallest = num3
  print(num1,num2,num3)
  print('The smallest number is: ',smallest)

if __name__ == '__main__':
    main()
