# Basic calculator:

print("***************************************************************")
print("\n\t=> Basic Calculator for Binary operation <=\t\n")
print("***************************************************************\n")

print("Press (1) for Addition")
print("Press (2) for Subtraction")
print("Press (3) for Multiplication")
print("Press (4) for Division")
print("Press (5) for Exponential")
print("Press (6) for Floor Division")
print("Press (7) for Modulus\n")

n = int(input('Enter here:'))

if n <= 7:
  num1 = int(input("Enter number1 -> "))
  num2 = int(input("Enter number2 -> "))
  if n == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
  elif n == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
  elif n == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
  elif n == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
  elif n == 5:
    print(f"{num1} to the power {num2} = {pow(num1, num2)}")
  elif n == 6:
    print(f"{num1} // {num2} = {num1 // num2}")
  elif n == 7:
    print(f"{num1} % {num2} = {num1 % num2}")    

else:
  print("\nxxxxx Please enter the number within given choice. xxxxx\n")