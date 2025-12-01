
numbers = [10,8,5,6,3,1,2,9,7]
ordenado = False
count = 1
while(not ordenado):
    ordenado = True
    for i in range(1,len(numbers)):
        count += 1
        if numbers[i-1] > numbers[i]:
            aux = numbers[i-1]
            numbers[i-1] = numbers[i]
            numbers[i] = aux
            ordenado = False

print(numbers)
print(count)
