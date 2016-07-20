#more printing

print " Mary had a little lamb"
print " Its flees was white as %s. " %'snow' #'snow' is actually not a variable, its just a string with the word  snow , a variable wouldn't have the single-quotes around it.
print " And everywhere that Mary went. "
print "." * 10 # What'd that do?

end1 = 'C'
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Whatch that comma at the end. try removing it so see what happens
print end1 + end2 + end3 + end4 +end5 + end6, #the comma enable two lines display in one line, one space between two line
print end7 + end8 + end9 + end10 + end11 + end12
# Couldn't you just not  use the comma, and turn the last two lines into one single-line print?
# Yes, you could very easily, but then it'd be longer than 80 characters, which in Python is bad style

