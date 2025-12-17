#empty set

s=set()
print(type(s))

# set methods (add,pop,clear,remove,union,intersection)

s.add(10)
s.add('sakshi')
s.add(25)
print(s)
s.add(30)
print(s)
# s.clear()   #makes set empty
# print(len(s))
s.pop()  #removes random value from set
print(s)
s.pop()
print(s)
s.remove(30) #error if element not present in set
print(s)

#union

set1={1,2,3,4}
set2={3,4,5,6,7}

print(set1.union(set2))

#intersection

print(set1.intersection(set2))


#Q.1 You are give a list of subjects for students. Assume one classroom is required for 1 subject.
#How many classrooms are needed by all students 
# subjects = python,java,c++,python,javascript, java,c++,c

#Ans :

subjects={'python','java','c++','python','javascript','java','c++','c'}
print(len(list(subjects)))

