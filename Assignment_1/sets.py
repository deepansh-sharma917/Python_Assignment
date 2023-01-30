s1={1,2,3}
s1.add(4) # adding elements in set
print(s1)
thisset=s1.copy()             #copy
thisset.clear()               #clear
print(thisset)
s2={4,5,6,7,8,2}
z=s1.difference(s2)            #difference
print(z)
y=s1.symmetric_difference(s2)  #symmetric difference
print(y)
print(s1.union(s2))        #union
s2.pop()                   #pop
print(s2)
print(s2.intersection(s1)) #intersection
print(s1.issubset(s2))   #issubset
print(s1.issuperset(s2)) #issuperset 
print(s1.isdisjoint(s2)) #disjoint 
