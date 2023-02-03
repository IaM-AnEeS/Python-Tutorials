grocery=["Harpic","vim bar", "deodrant","Vegitables","Rice","Sugar"]
print(grocery[4])
numbers=[222,43,52,60,12,1,4,2,3]
number=[]
# numbers.sort()
# numbers.reverse()
number.append(2)#Apped use to add the number in the end
number.append(3)
number.append(4)
number.append(5)
numbers.insert(1,94)# This will insert the element where you want to add
numbers.remove(222)
numbers.pop()#This will remove last element inside the list
print(numbers)
print(numbers[0:9])
print(numbers[:9])
print(numbers[:])
print(numbers[0:])
print(numbers[0:8])
print(numbers[0:8:1])#By default 1
print(numbers[0:8:2])
print(numbers[::-1])#This will reverse the List
print(max(numbers))
print(min(numbers))
print(len(numbers))
numbers[3]=91
print(numbers)

# mutable==can Change
# Imutable==cannot Change
# List is mutible
# tuple is imutible
tp=(1,2,4)
tp=(1,)
# tp[1]=67
print(tp)#Canr Change
# Swapping logic
a=2
b=4
temp=a
a=b
b=temp
print(a,b)
# Python way of Swaping
a,b=b,a
print(a,b)


