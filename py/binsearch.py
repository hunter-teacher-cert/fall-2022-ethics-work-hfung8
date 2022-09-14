# binsearch.py
# Harrison Fung 
# CSCI 77800 Fall 2022
# collaborators: Harrison Fung
# consulted: 

# assign low, mid and high 
import random
def binarySearch(arr, value):
  low = 0
  high = len(arr)-1
  mid = 0
  
  while (low <= high):
    mid = (low + high)//2
    if (arr[mid] == value):
      return mid
    elif (value < arr[mid]):
      high = mid - 1 
    else:
      low = mid + 1

def listSearch():
  randomList = []
  for i in range(0,5):
    n = random.randint(0,10)
    randomList.append(n)
  return randomList

newList = listSearch()

def sortList(list):
  for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
      if (list[i] > list[j]):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
  return list
    

print(newList)
sortedList = sortList(newList)
print(sortedList)

# search for the number 5
binaryList = binarySearch(sortedList, 5)
print(binaryList)


