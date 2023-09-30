arr=list(map(int,input().split()))
mx=max(arr)
myList=[]
for i in arr:
    if i < mx:
        myList.append(i)
print(max(myList))


  
            
  


