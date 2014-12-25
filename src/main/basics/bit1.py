from sys import argv
script,filename=argv
mylist = [1, 2, 3, 4]
input1=raw_input("enter additional numbers /n")
txt=open(filename,'w')
total = 0
for number in mylist:
    total = total + number

	
print "The sum of the numbers is:", total+int(input1)

target.write=total+int(input1)