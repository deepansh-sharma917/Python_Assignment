lst=[1,2,3,4]
lst2=["Rajesh","Ramesh","Suresh"]
print(len(lst)) # length of list
# append method
lst.append("Hello")
lst.append(True)
print("The values after adding in list",lst)
# extend method
lst.extend([7,8])
print(lst)
# insert method
lst.insert(3,"Deepansh")
print(lst)
# Delete element using remove
lst.remove(2)
print(lst)
#Reverse the list
lst.reverse()
print(lst)
#Delete element using pop
lst.pop()
print(lst)
#index
print(lst.index("Hello"))
#slicing
print(lst[:3])
print(lst2.index("Ramesh"))
