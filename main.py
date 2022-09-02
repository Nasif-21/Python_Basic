import re
#Importing regular expression

word="I am not Fine"
word2="I am much much fine"
word3="Welcome to Python Compiler Design"
word4="Iamsosad"
a=re.search("^I",word)
b=re.search("^The",word)
c=re.search("^I.*Fine$",word)  #(^)Word starts with I and ends($) with Fine and ($) 0 occurance
d=re.findall("m",word2) #Find all the M
e=re.findall("good",word2) #If they found no match, return a blank
f=re.search("to",word3) #Finding the position of the word to
g=re.split("",word3) #Splitting every word
h=re.sub(""," ",word4) #Substituting
i=re.sub(""," ",word4,2) #Using Index

if a:
    print("Word found")
else:
    print("Not Found")

if b:
    print("Word found")
else:
    print("Not Found")

if c:
    print("Word found")
else:
    print("Not Found")

print(d)
print(e)
print("Position of the word to is in",f.start())
print(g)
print("Before Splitting")
print(word4)
print("After Splitting")
print(h)
print(i)
