name=["Sheikh","Muhtasim","Nasif"]
print(name)
print(name[0])
print(len(name)) #length of array

for n in name:    #array looping
    print(name)

name.append("Shitab") #adding an element
print(name)

name.pop(3) #remove a data using index number
print(name)

name.remove("Muhtasim")
print(name)

number=[20,60,33,48,96]
print(number.count(20)) #specifing individual index
number.reverse()
print(number)
number.sort()
print(number)
name.extend(number)  #Adding 2 array elements
print(name)

