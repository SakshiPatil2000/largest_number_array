class Solution:
    def largestOfNumbers(self,a:int,b:int,c:int,d:int) -> int :
        largest= a
        
        if(b>largest):
            largest=b
        if(c>largest):
            largest=c
        if(d>largest):
            largest=d
            
        return largest
    
#User input 
a=int(input('Enter 1st number :'))
b=int(input('Enter 2nd number :'))
c=int(input('Enter 3rd number :'))
d=int(input('Enter 4th number :'))

sol =Solution()

result=sol.largestOfNumbers(a,b,c,d)

print("Largest of four numbers is :",result)