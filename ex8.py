formatter = "%r %r %r %r"                                         # set the variable "formatter" to a string with four raw-formatter signs

print formatter % (1, 2, 3, 4)                                    # print out the variable "formatter" with the formatters "1", "2", "3", "4"
print formatter % ("one", "two", "three", "four")                 # print out the variable "formatter" with the formatters "one", "two", "three", "four" 
print formatter % (True, False, False, True)                      # print out the variable "formatter" with the formatters "True", "False", "False", "True"
print formatter % (formatter, formatter, formatter, formatter)    # print out the variable "formatter" with the formatters "formatter", "formatter", "formatter", "formatter"
print formatter % (                                               # print out the variable "formatter" with the four sentences as formatters
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
  )
