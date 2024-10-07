ll = int(input("Enter the size of array: "))
pp = []
count = 0

for num in range (ll):
    ss = int(input("Enter the number: "))
    pp.append(ss)
for num in pp:
    count += num ** 2
       

print(count)    