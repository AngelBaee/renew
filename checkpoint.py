time = int(input("Enter the range of times: "))

list = []

count = 0

for i in range(time):
    actual = int(input("Enter the time: "))
    list.append(actual)
    count += actual // 2

print(count)    