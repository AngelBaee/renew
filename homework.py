numb = int(input("Enter the size of array: "))

arr = []

for i in range (numb):
    numb2 = int(input("Enter the number: "))
    numb2 *= 2
    arr.append(numb2)

print(arr)