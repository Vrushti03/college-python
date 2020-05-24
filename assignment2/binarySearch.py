list=input("Enter sorted list of elements seperated by space ")
list=list.split()
n=input("Enter the number to search")

def binary_search(list,n):
  start = 0
  end = len(list)
    
  while start < end:
    mid = (start + end)//2
    if list[mid]>n:
      end=mid
    elif list[mid]<n:
      start=mid+1
    else:
      return mid
  return -1    
    
index=binary_search(list,n) 
if index<0:
  print("Not found")
else:
  print("{} found at {}".format(n,index))
    
