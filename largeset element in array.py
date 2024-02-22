size = int(input("enter the size of array:"))
arr=[]
for i in range(size):
    element=int(input())
    arr.append(element)
print("the array is:",arr)
large=arr[0]
for i in arr:
    if i > large:
        large = i
print(large)
