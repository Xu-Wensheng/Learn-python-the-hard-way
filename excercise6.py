# string and text

x = "There are %d types of people." %10
binary = "binary" # there exists string varables in Python
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print " I said: %r. " % x
print " I also said: '%s'" %y

hilarious = False
joke_evaluation = " Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = " This is the left side of..." #string varables can be calculated like numbers
e = " a string with a right side"

print w+e

# What's the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are actually displaying variables to users.

# What's the difference of between %r and %s
# Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.

