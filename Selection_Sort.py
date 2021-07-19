#Implementation of Selection Sort in Python
#Finding minimum value from the left to right and replace with currect value

l=[40,29,30,55,70,18,35]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            l[i],l[j]=l[j],l[i]
print(l)



#  Or you can do it in another way

def selectionSort(l):
  for i in range(len(l)-1):
    for j in range(i+1,len(l)):
      if l[j]<l[i]:
        l[i],l[j]=l[j],l[i]
  return l
list1=[40,29,30,55,70,18,35]
print(selectionSort(list1))
