from sys import argv
script,filename1,filename2=argv

print " The source file name is %r :" %filename1
print " The target filename is  %r:" %filename2

raw_input("?")

print "Opening the source and target files..."
source=open(filename1,'r')
target=open(filename2,'w+')

print "Truncating the target file..%r" %filename2

target1=source.read()

print " Writing the target file or copying from source to target"

target.write (target1)

print "Hopefully its copied now"
target.close()