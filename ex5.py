name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_metric = height * 2.54
weight = 180 # lbs
weight_metric = weight * 0.4536
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actuelly that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "The metric values for the height and the weight are \nheight: %s \nweight: %s" %(height_metric, weight_metric)
