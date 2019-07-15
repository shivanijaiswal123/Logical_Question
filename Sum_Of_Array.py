import random 

n = int(input("Enter size of array:-"))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x) 
    
print("array is:",arr)

#Sum of the whole array

sum=0

for index in range(len(arr)):
    sum=sum+arr[index]
print("The Sum of Array is:",sum)