x = "There are %d types of people." %10                         # set the variable "x" to a string with the formater "10"
binary = "binary"                                               # set the varibale "binary" to the string "binary"
do_not = "don't"                                                # set the variable "do_not" to the string "don't"
y = "Those who knows %s and those who %s." % (binary, do_not)   # set the varibale "y" to a string with the formater "binary" and "do_not"

print x                                                         # print out the value of the variable "x"
print y                                                         # print out the value of the varibale "y"

print "I said: %r" % x                                          # print out a string with the formater "x"
print "I also said: '%s'." % y                                  # print out a string with the formater "y"

hilarious = False                                               # set the varibale "hilarious" to the value "False"
joke_evaluation = "Isn't that joke so funny?! %r"               # set the varibale joke_evaluation to a string with a r-formater

print joke_evaluation % hilarious                               # print out the string of the variable "joke_evaluation" with the formater "hilarious"

w = "This is the left side of..."                               # set the varibale "w" to a string
e = "a string with a right side."                               # set the varibale "e" to a string

print w + e                                                     # print out the contacanation of the varibales "w" and "e"
