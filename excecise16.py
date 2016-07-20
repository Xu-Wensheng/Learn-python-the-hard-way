#reading and writing files

# close: close the file. like  File->Save.. in your editor
# read: reads the contents of your file. you can assign the result to a variable
# readline: reads just one line of a text file
# truncate: empties the file. watch out if you care about the file
# write('stuff'): writess "stuff"to the file

from sys import argv

script, filename = argv

print " We're going to erase %r." %filename
print " If you don't want that, hit CTRL-C (^C)."
print " If you do want that, hit Enter."

raw_input("?")

print " Opening the file...."
target = open(filename, 'w')

print " Truncating the file. Goodbye!"
target.truncate()

print " Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print " I'm going to write three to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)  
target.write("\n")

print " Add finally, we close it."
target.close()

