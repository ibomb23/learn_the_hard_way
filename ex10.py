tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
  I'll do a list:
  \t* Cat food
  \t* Fishies
  \t* Catnip\n\t* Grass
  """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

triple_single_quote = '''What a spring...'''
triple_double_quote = """What a spring..."""

print "%s \\ this is to \'BIG\" %s me!" %("This", 4)
print "\a what is that"
print "an this \b"
print "\f i dont know"
print "\N{DIVISION SIGN}"
print "\r i try it all \t i mean all!"
print "\N{THAI CHARACTER KHO KHON}
print "\uFFFF"
print "\UFFFFFFFF"
print "\v"
