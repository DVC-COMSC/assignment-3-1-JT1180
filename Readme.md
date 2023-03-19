[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10482266)
<!--
[Link to Chap 5 Lab18](https://docs.google.com/presentation/d/1r3h2R9JwK9HK_U2Ia-zncL0BSjHV6Giu6ugNJ6yZpgc/edit#slide=id.g1715447b552_0_27)

![Lab 16](https://nimbus-screenshots.s3.amazonaws.com/s/e634571b38c8923031df60fc7fc2fe3f.png)
-->

## Complete the "main.py"

Explanation

  num1, num2, and num3 are all set to display any random number between 0-100 where it will then be calculated to find and display which of the three is numbers is the smallest

Code
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

Output
  The number that is found to be the smallest is displayed here