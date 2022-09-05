newfile=open("E:\Python Basics\Filework\Secret.txt") # opening a file for reading
print(newfile.read())
newfile.close()

newfile2=open("E:\Python Basics\Filework\Laboh ko.txt.txt","a") #using append, a file is created
newfile2.write("Labon Ko Labon Pe Sajao")
newfile2.write("Kya Ho Tum Mujhe Ab Batao")
newfile2.write("Todh Do Khud Ko Tum")
newfile2.write("Banhon Mein Meri *3 ")

newfile2.close()
newfile2=open("E:\Python Basics\Filework\Laboh ko.txt.txt","r")
print(newfile2.readline())
print(newfile2.readline())
print("Not a good option though")
newfile2=open("E:\Python Basics\Filework\Laboh ko.txt.txt","r") #To read line by line
for song in newfile2:
    print(song)