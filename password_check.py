password=str(input("Enter a password:"))
no_alphabets=0
no_digits=0
no_spaces=0
no_specialchar=0
for i in password:
    if i.isalpha()==True:
        no_alphabets+=1
    elif i.isdigit()==True:
        no_digits+=1
    elif i.isspace()==True:
        no_spaces+=1
    else:
        no_specialchar+=1

for i in password:
        if len(password)>=12 and no_alphabets>=1 and no_digits>=1 and no_specialchar>=1: 
               print("This is a valid password")
               break
        else:
             password=input("Invalid password.Please enter a valid password:")

