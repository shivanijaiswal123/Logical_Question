import random 

n = int(input("Enter size of array:-"))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x) 
    
print("array is:",arr)

#largest number from the array

max=random.choice(arr)

for index in range(len(arr)):
    if max<arr[index]:
        max=arr[index]
        
print(max)