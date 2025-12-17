# print numbers from 1 to 100

i=1
while i<=100:
    print(i)
    i +=1
print('loop ended')

# print numbers from 100 to 1

i=100
while i>=1:
    print(i)
    i -=1
    
print('loop ended')

# print multiplication table of number n

n = 5
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

# print elements of the list using loop

squares=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(squares):
    print("Element at index",i,"is :",squares[i])
    
    i +=1

# search for a number x in this tuple using loop

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
check = 49
found = False

while i < len(numbers):
    if numbers[i] == check:
        print(check, "is found")
        found = True
        break
    i += 1

if not found:
    print(check, "is not found")

     

# 1.use of continue

i=1
while i<=10:
    if i==5:
        i +=1
        continue
    print(i)
    i +=1
# 2. even number using continue

i=1
while i<=10:
    if i%2 != 0:
        i +=1
        continue
    print(i) 
    i +=1 
    
# 3. odd number using continue

i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1

    
    