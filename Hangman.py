import random
st6="+------+\n |\t|\n O\t|\n/|\     |\n/ \     |\n\t|\n\t|\n\t|\n==========\n"
st5="+------+\n |\t|\n O\t|\n/|\     |\n/       |\n\t|\n\t|\n\t|\n==========\n"
st4="+------+\n |\t|\n O\t|\n/|\     |\n        |\n\t|\n\t|\n\t|\n==========\n"
st3="+------+\n |\t|\n O\t|\n/|      |\n        |\n\t|\n\t|\n\t|\n==========\n"
st2="+------+\n |\t|\n O\t|\n |      |\n        |\n\t|\n\t|\n\t|\n==========\n"
st1="+------+\n |\t|\n O\t|\n        |\n        |\n\t|\n\t|\n\t|\n==========\n"
li=[st6,st5,st4,st3,st2,st1]
print("Welcome to the Hangman game!!")
st_user1=random.choice(["hello","mekso","loop","tarzan"])
correct_ans=[]
lives=6
for i in st_user1:
   correct_ans+="_"
n=0
while True:
    st_user2=input("Guess the letters of the word: ").lower()
    for n in range(len(correct_ans)):
      letter=st_user1[n]
      if letter==st_user2:
        correct_ans[n]=st_user2
    print(correct_ans)
        
        
    if st_user2 not in st_user1:
       lives-=1
       print(li[lives])
       print(f"Wrong answer!{lives} lives remaining!")

        
    if lives==0:
        print("GAME OVER...!!")
        break
    if correct_ans==list(st_user1):
        print("Hurray! You Win!")
        break

        






































































