from sys import argv
script,filename=argv

txt= open(filename) # or use open(filename,w) for write mode

print "Here is the name of the file %s" % filename
print txt.read()
txt.close()	
print "Type the filename agagin :"
file_again=raw_input("> ")
txt_again=open(file_again)

print txt_again.read()