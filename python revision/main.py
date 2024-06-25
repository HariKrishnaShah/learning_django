import json
import math
import datetime
import my_module
import my_module as greet
import platform
from my_module import cost as mymoduleCost
import re
import numpy
print("Hello")
x = 40
print(x)

arr = [1,2,3,4,5]
print(arr)
arr.append(6)
print(arr)
arr.insert(1, 99)
print(arr)
arr.remove(4)
print(arr)
arr.pop(1)
print(arr)
# arr.clear()
print(arr)
print(type(arr))
newarr = [8,9,10]
combarr = arr + newarr
print(combarr)
newarr[:0] = [55,55]
print(newarr)
newarr[1:2] = [88,99,100,101,105]
print(newarr)
print(newarr[2])
print(newarr[0:2])
fruits = ["apple", "banana"]
# arr.extend(fruits)
# print(arr)
for x in fruits:
    arr.append(x)
print(arr)
print(arr.count("apple"))
zz = arr.copy()
zz.reverse()
print(arr)
print(zz)
# zz.sort()
# print(zz)
newarr.sort()
print(newarr)
newarr.reverse()
print(newarr)
newarr.sort(reverse=True)
print(newarr)
print(fruits)
fruits.sort(reverse= True, key= str.lower)
print(fruits)
print(fruits[-1])

newTuple = ("a","b","c")
print(newTuple)
print(newTuple[1])
changeList = list(newTuple)
changeList[1] = "f"
newTuple = tuple(changeList)
print(newTuple)
(a, *all) = changeList
print(a)
print(all)
(x, *y) = arr
print(x)
print(y)
obj = {"name":"Hari", "address":"sindhuli"}
obj2 = {**obj}
print(obj2)
for x in range(len(fruits)):
    print(fruits[x])
i = 0
while i<len(fruits):
    print(fruits[i])
    i+=1

for x in [0,1]:
    print(fruits[x])

tuple1 = ("a", "b")
tuple2 = (1,2)
tuple3 = tuple1 + tuple2
print(tuple3)
tuple3 = tuple1 * 4
print(tuple3)
print(tuple3.count("a"))
print(tuple3.index("b"))
set1 = {"apple", "banana", "kiwi"}
print(set1)
# set doesn't allow duplicate values
set2 = {"apple", "banana", "kiwi", "kiwi"}
print(set2)
print("apple" in  set1)
# in search is case sensitive
print("Apple" in set1)
set1.add("watermelon")
print(set1)
set3 = {"Papaya, coconut"}
set1.update(set3)
print(set1)
arr = [8,9,10]
(x, *y)= [8,9,10]
print(x)
print(y)
print({**obj2})
print(set2)
set2.remove("apple")
set2.discard("kiwi")
set2.add("mango")
print(set2)
for x in set2:
    print(x)
fruitsSet1 = {"apple", "mango", "kiwi"}
fruitsSet2 = {"coconut", "apple", "orange"}
unionSet1 = fruitsSet1.union(fruitsSet2)
print(unionSet1)
intersectionSet1 = fruitsSet1.intersection(fruitsSet2)
print(intersectionSet1)
unionSet2 = fruitsSet1 | fruitsSet2
print(unionSet2)
unionSet3 = fruitsSet1.union(arr)
# True and 1 is treated as duplicates in set
unionSet3.add(True)
unionSet3.add(1)
print(unionSet3)
intersection2 = fruitsSet1 & fruitsSet2
print(intersection2)
differenceSet1 = fruitsSet1.difference(fruitsSet2)
print(differenceSet1)
differenceSet2 = fruitsSet2.difference(fruitsSet1)
print(differenceSet2)
differenceSet3 = fruitsSet2 - fruitsSet1
print(differenceSet3)
# set difference only work with sets
# differenceSet4 = fruitsSet2 - arr
# print(differenceSet4)
symmetricDifference = fruitsSet1.symmetric_difference(fruitsSet2)
print(symmetricDifference)
fruitsSet1.symmetric_difference_update(fruitsSet2)
print(fruitsSet1)
fruitsSet1.difference_update(fruitsSet2)
print(fruitsSet1)
fruitsSet2.intersection_update(fruitsSet1)
print(fruitsSet2)
fruitsSet2 = fruitsSet1.copy()
print(fruitsSet1)
set1.update(fruitsSet2)
print(set1)
set1.update(arr)
print(set1)
set1.symmetric_difference_update(changeList)
print(set1)
set1.difference_update(changeList)
print(set1)
print(set1.isdisjoint(set2))

mydict = {"name":"Hari", "address":"Sindhuli"}
print(mydict)
print(mydict["name"])
mydict["phone"] = 9844523112
print(mydict)
print(len(mydict))
mydict["fav-food"] = ["biryani", 'oatmeal']
print(mydict)
mydict2 = dict(name = "Rahul", address = "Bagmati")
print(mydict2)
print(mydict.get("address"))
keys = mydict.keys()
values = mydict.values()
items = mydict.items()
print(keys)
print(values)
print(items)
mydict["address"] = "Nepal"
print(mydict)
mydict.update({"address":"Madhutar"})
print(mydict)
mydict.update({"fav-person":"Khagi"})
print(mydict)
mydict.pop("address")
print(mydict)
mydict.popitem()
print(mydict)
print(mydict2)
mydict2.clear()
print(mydict2)

for x in mydict:
    print(x)

for x in mydict:
    print(x + " : " + str(mydict[x]))
    if(x == "fav-food"):
        for y in mydict[x]:
            print(y)
for x in mydict.values():
    print(x)
for x in mydict.keys():
    print(x)
print("key-value")
for x, y in mydict.items():
    print(x + ":"  + str(y))
    
print("items print")
for x in mydict.items():
    print(x)

mydictCopy1 = mydict.copy()
mydictCopy2 = dict(mydict)
mydictCopy3 = {**mydict}
print(mydictCopy1, mydictCopy1 == mydict, mydictCopy1 is mydict)
print(mydictCopy2, mydictCopy2==mydict, mydictCopy2 is mydict)
print(mydictCopy3, mydictCopy3==mydict, mydictCopy3 is mydict)
variable1 = mydict.setdefault("love", "Khageshwari")
print(variable1)

vegetable1 = {"name":"Cucumber", "color":"green"}
vegetable2 = {"name":"cauli", "color":"greenish white"}
vegetable3 = {"name":"chili", "color":"red"}
vegetableDict = {
    "item1":vegetable1,
    "item2": vegetable2,
    "item3": vegetable3
}
print(vegetableDict)
print(vegetableDict["item2"]["name"])
for x, obj in vegetableDict.items():
    print(x)
    for y,z in obj.items():
        print(y + " : " + str(z))

keys = ("name", "address", "phone")
value = ("Hari")
# same value is passed to every key
newDict = dict.fromkeys(keys, value)
print(newDict)

a = 99**5
b = 20**8
c = 10**5
if(a>b):
    if(a>c):
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if(b>c):
        print("b is greatest")

if(a>b):
    print("a is greater than b")
elif(b>a):
    print("b is greater than a")

if(a>b and a>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest") 
elif(c>a and c>b):
    print("c is greatest")

if(a>b or a>c):
    print("a is greater than either b or c")

print("a") if(a>b) else print("=") if (a==b) else print("b greater than a")

print("a is greatest") if(a>b) and (a>c) else print("b is greatest") if(b>a) and (b>c) else print("c is greatest")


for x in range(len(arr)):
    print(x)


try:
    # cost = (input("Enter the cost: "))
    cost = 10
    if(isinstance(cost, float)):
        raise TypeError("The enter value is not a number")
    if(float(cost)<0):
        raise ValueError("Entered value is lesser than 0")
    msg = f"The cost is {float(cost):,.2f}"
    print(msg)
except TypeError as err:
    print("An error occured while printing cost. Err: " + str(err))
except ValueError as err:
    print("An error occured. Err: " + str(err))
except Exception as err:
    print("Error occured. Err: " + str(err)) 
else:
    print("Successful. No error occured")
finally:
    print("Completed execution")

x =  '{ "name":"Hari", "age":25, "city":"Sindhuli"}'
z = json.loads(x)
print(z)
print(type(z))
print(type(x))
newJson = json.dumps(z)
print(newJson)
print(type(newJson))
# we can not access value of json object in this way
# print(newJson["name"])
# We can access values of dictionary in this way
print(z["name"])
for a,b in z.items():
    print(a ,": " , b)

print("Min is" , min(10,20,5,100,105))
print("Max is " , max(10,20,5,100,105))
print("5 to power 2 is ", pow(5,2))
print("sqrt of 81 is " , int(math.sqrt(81)))
print("ceil of 1.8 is " , math.ceil(1.8))
print("floor of 1.8 is ", math.floor(1.8))
print("round upto 2 decimal of 1.82563 is ", round(1.82563, 2))
print("round upto 3 decimal of 1.82563 is ", round(1.82563, 3))
print("round upto 4 decimal of 1.82563 is ", round(1.82563, 4))
print("Value of pi is " , math.pi)

currentTime = datetime.datetime.now()
print("Current time is ", currentTime)
print(currentTime.strftime("%H:%M"))
print(currentTime.strftime("%d/%m/%Y"))
print(dir(math))
my_module.printName("Hari")
greet.printName("Rahul")
print("The cost is " + str(my_module.cost))
x = platform.system()
print(x)
print("Imported cost is " + str(mymoduleCost))

x = 2000
def myFun1():
    x = 100
    print("Value of x inside func is " , x)
myFun1()
def myFunc2():
    print("Value of x is " , x)
myFunc2()
def myFunc3():
    global x
    x = 25
    print("value of x is ", x)
myFunc3()
print(x)

def myFunc4():
    x = 45
    print("Value of x in func4 is ", x)
    def myFunc5():
        print("value of x in func5 is ", x)
    myFunc5()
myFunc4()
print("Value of x after func4 call is ", x)

def myFunc6():
    x = 45
    print("Value of x in func6 before other func call is ", x)
    def myFunc7():
        nonlocal x
        x = 22
        print("Value of x in func7 is ", x)
    myFunc7()
    print("value of x in func6 after func7 call is ", x)
myFunc6()
print("value of x after func6 call is ", x)

string = "Hello I am Hari"
split = re.split("\s", string)
print("splitted string is: ")
print(split)
replaced = re.sub("H", "k", string)
print("Replaced 'H' with 'k' in string: ")
print(replaced)
findA = re.findall("a", string)
print("Found a:")
print(findA)
print("Count of a in string is ", string.count("a"))
print("Count of a in string through regex is ", len(findA))
z = re.search(r'i$', string)
print("Does string end with i? : ", bool(z))

def myFunc8(n):
    return lambda a: n + a

newSkip15  = lambda a, b: a + b + 10
print("newSkip15")
print(newSkip15(0, 5))
print(newSkip15(10, 5))
print(newSkip15(20, 5))
skip10 = myFunc8(10)
print(skip10(0))
print(skip10(10))
print(skip10(20))

my_arr = [1,2,3]
tupleArr = (1,2,3)
def myFunction(arr):
    arr[0] = 44
    return arr[0]
print(myFunction(my_arr))
print("Value of array after function call is :")
print(my_arr)

# Passing values as a tuple arr
def myFunction2(*arr):
   
    return arr[0]
print(myFunction2(8,9,10))
print("Value of my_arr after function call is : ", my_arr)

def myFunction3(**arr):
    arr['fname'] = "Hari"
    return arr['fname']

print(myFunction3(fname = "Rahul", lname = "shah"))


def myFunction4(a = 5):
    return a + 5

print(myFunction4())
print(myFunction4(10))

def myFunction5(x,y,z):
    return {"x":x, "y":y, z:z}
print(myFunction5("Hari", "Krishna", "Shah"))
print(myFunction5(x = "Rahul", y = "Kumar", z = "shah"))

def myFunction6(x, y, /, *, z):
    return {"x":x, "y":y, z:z}
print(myFunction6("Shaym", "Kumar", z = "Shah"))

def myFunc10(n):
    if(n<=0):
        return 0
    else:
        return (n + myFunc10(n-1))

print("Sum of natural numbers upto 10 is ", myFunc10(10))

fruits = ["apple", "banana", "orange"]
myiterate = iter(fruits)
print(next(myiterate))
print(next(myiterate))
print(next(myiterate))
# print(next(myiterate))

class iterateNumber:
    def __iter__(self):
        self.number = 10
        return self
    def __next__(self):
        if self.number <= 200:  
            x = self.number
            self.number *=10
            return x
        else:
            raise StopIteration

myObj = iterateNumber()
myiter = iter(myObj)
try:
    
    
     
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
except Exception as err:
    print(err)

for x in myiter:
    print(x)

class Vehicle:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def move(self):
        print("Can Move")

class Car(Vehicle):
    def __init__(self, name, cost):
        super().__init__(name, cost)
    def move(self):
        print("Car can ride")

class Aeroplane(Vehicle):
    def __init__(self, name, cost):
        super().__init__(name, cost)
    def move(self):
        print("Aeroplane can fly")

class Boat(Vehicle):
    z = 20
    def __init__(self, name, cost):
        self.x = 55
        super().__init__(name, cost)
    def move(self):
        print("Boat can Sail")
        
car = Car("Lamborgini", 50000000)
aeroplane = Aeroplane("Airbus", 532000000)
boat = Boat("Huricanna", 9000000)
car.move()
aeroplane.move()
boat.move()
print(boat.z)
print(boat.x)
arr = numpy.array([8,9,10])
print(arr)
print(type(arr))
print(arr[2])

arr = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,8,8]])
print(arr.shape)
newarr = arr.reshape(2,6)
print(newarr)
newarr = arr.reshape(12)
print(newarr)
print(newarr.base)
print("View or Copy")
print(arr.reshape(1, 12).base)
newarr[0] = 999
print(newarr)
print(arr)
arr2 = numpy.array([[88,88,88,88]])
finalArr = numpy.concatenate((arr, arr2))
print(finalArr)
newarr = numpy.split(arr, 3)
print(newarr)
print(newarr[1])
arr = numpy.array([1,8,5,8,9,10,8])
positions = numpy.where(arr ==8)
print(positions)
print(numpy.sort(arr))
print(arr)

condition = arr >5
print("condition")
print(condition)
print(type(condition))
filteredArr = arr[condition]
print(filteredArr)
index = 2
print(arr[2])
condition1 = arr[[True, False, False,False,False,False,False]]
filteredArr2 = arr[condition1]
print(filteredArr2)

