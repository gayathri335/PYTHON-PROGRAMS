len=int(input("enter the size of array:"))
arr=[]
for i in range(len):
    element=int(input())
    arr.append(element)
print("array is:",arr)

#multiplication of array
mul=arr[0]
for i in arr:
    mul=arr[0] * i
n=int(input("enter the n value:"))
rem=mul%n
print("the output is:",rem)
