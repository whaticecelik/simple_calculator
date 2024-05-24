num1 = int(input("enter the first number for your calculation: "))
num2 = int(input("enter the second number for your calculation: "))
op = str(input("enter '+' for addition, '-' for subtraction , '*' for multiplication, '/' for divison: "))
total = ''

if op == '+':
  total = num1 + num2
  print(str(num1)+' '+ str(op) +' '+ str(num2) +' = ' + str(total))
elif op == '-':
  total = num1 - num2
  print(str(num1)+' '+ str(op) +' '+ str(num2) +' = ' + str(total))
elif op == '*':
  total = num1 * num2
  print(str(num1)+' '+ str(op) +' '+ str(num2) +' = ' + str(total))
elif op == '/':
  if num2 == 0:
    print("Error! Divison by zero! Please enter a possitive number.")
  else:
    total = num1 / num2
    print(str(num1)+' '+ str(op) +' '+ str(num2) +' = ' + str(total))