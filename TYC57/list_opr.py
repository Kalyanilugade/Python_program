#list oprations

lst=["Apple","banana","mango"]
lst.append("orange")
print(lst)

shake=lst.copy()
print("colpied list",shake)
print("clear",shake.clear())
print("count",lst.count("banana"))

car=["BMW","THAR","ARTICA"]
other_cars=["AUDI","BOLERO"]
car.extend(other_cars)
print(car)
print("index",car.index("AUDI"))

lst2=[1,2,3,4]
lst2.insert(4,"6")
print(lst2)
print("pop",lst.pop())

list1=['a','b','c']
list1.remove('a')
print(list1)
list1.reverse()
print(list1)


list2=[1,2,3,4,5]
list2.reverse()
print(list2)
