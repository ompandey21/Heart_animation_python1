
def leapYear(x):
  if x%4==0 and x%100!=0 or x%400==0:
    print(f"{x} is a leap year")
  else:
    print(f"{x} is not a leap year")

def factorial(a):
  f=1
  for n in range(1,a):
    f*=n
  print(f)   

def primeNumber(b):
  no_divisors=0
  for m in range(1,b+1):
    if b%m==0:
      no_divisors+=1
    else:continue
  if no_divisors==2:
    print(f"{b} is a prime number")
  else:
    print(f"{b} is not a prime number")

def palindrome(s):
  new_s=str(s)
  new_s1=new_s[::-1]
  if new_s==new_s1:
    print("This is a palindrome number")
  else:print("This is not a palindrome number")

while(True):
  print()
  print("Function Menu:")
  print("1.Check Leap Year")
  print("2.Calculate Factorial")
  print("3.Check Prime Number")
  print("4.Check Palindrome")
  print("5.Exit")
  user_pref=int(input("Enter your choice(1-5): "))
  if user_pref==1:
    year=int(input("Enter the year: "))
    leapYear(year)
  elif user_pref==2:
    number1=int(input("Enter the number: "))
    factorial(number1)
  elif user_pref==3:
    number2=int(input("Enter the number: "))
    primeNumber(number2)
  elif user_pref==4:
    number3=int(input("Enter the number: "))
    palindrome(number3)
  elif user_pref==5:
    print("Thank you!")
    break
  else:print("Invalid Input")



