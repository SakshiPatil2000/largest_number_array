# print numbers from tuple

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in numbers :
    print(num)
    
#serach for number x in tuple

squares = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,49)

x=49
index=0

for num in squares:
    if num == x :
        print(x,"found at index : ",index)
        # break
    index +=1

# create a list of numbers using range

n=5
num=[]

for i in range(n):
    value =int(input('Enter number :'))
    num.append(value)
    
print(num)

# examples with range()

for i in range(5) :
    print(i)      #default 0 is taken as start number
    
print('With start and stop')
for j in range(1,5):
    print(j)
 
print('With start, stop and increment')   
for k in range(1,10,2):
    print(k)
    
nameList=['sakshi','vishu','shree']

print('List with index and corresponding element')
for name in range(len(nameList)):
    print(name,nameList[name])
    
#pass

for i in range(5):
    pass
print("No work inside loop")

for i in range(3):
    if i == 1:
        pass
    print(i)

    