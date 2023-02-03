s=set()
print(type(s))
l=[1,2,3,4]
s_from_list=set(l)
print(s_from_list)
# s.add(1)
# s.add(2)
# s.add(1)# These two are not 
# s.add(2)# gona add bcz set take only unique value
# s.add(5)
s1=s_from_list.intersection({1,2,3,4,5,6,7,8,9,10})
print(s_from_list,s1)
s1=s_from_list.union({1,2,3,4,5,6,7,8,9,10})
print(s_from_list,s1)
print(max(s1))
print(min(s1))
print(len(s1))
print(s_from_list.isdisjoint(s1))