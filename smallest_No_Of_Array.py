import random 

n = int(input("Enter size of array:-"))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x) 
    
print("array is:",arr)

#largest number from the array

minimum=random.choice(arr)

for index in range(len(arr)):
    if minimum>arr[index]:
        minimum=arr[index]
        
print("The largest No of Array is:",minimum)