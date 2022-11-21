string1=input()
string2=input()
k=string2[-1]
count=0
for i in string1:
  if i==k:
    count+=1
print(count)
