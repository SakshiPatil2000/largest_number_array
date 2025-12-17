# WAP of sum of 2 numbers using funtion

def sumOfNumbers():
    a=5
    b=10
    print('Sum of',a,' and ',b ,'is :',a+b)
    
sumOfNumbers()

 # WAP of substraction of 2 numbers using funtion
 
def substractionOfNumbers(a : int , b : int) -> int:
     sub = a-b
     return sub
 
print('Substraction of two numbers is:',substractionOfNumbers(10,5))

#WAP to calculate average of three numbers

def averageCalculation(a:int, b:int, c:int) -> int :
    average = (a+b+c)/3
    return average

a=int(input('Enter value of 1st number :'))
b=int(input('Enter value of 2nd number :'))
c=int(input('Enter value of 3rd number :'))

print("Average of these numbers is :",averageCalculation( a,b,c))


#WAP to calculate average of three numbers using list

def averageCalculationListNumbers(*nums) :
    average = sum(nums)/len(nums)
    return average

numbers=[]

for i in range(3):
    value =int(input('Enter number :'))
    numbers.append(value)
    
print('Average of numbers in list is :',averageCalculationListNumbers(*numbers))


# WAP to print key value pairs

def dictionaryData(**details):
    for key,value in details.items():
        print(key,value)
        
dictionaryData(name='sakshi',role='Full Stack Mobile Developer')
    