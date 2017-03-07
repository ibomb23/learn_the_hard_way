cars = 100                                              #set the variable "cars" equal to 100
space_in_a_car = 4.0                                    #set the variable "space_in_a_car" equal to 4.0
drivers = 30                                            #set the variable "drivers" equal to 30
passengers = 90                                         #set the variable "passengers" equal to 90
cars_not_driven = cars - drivers                        #set the variable "cars_not_driven" eqaul the balance of variable "cars" and variable "drivers"
cars_driven = drivers                                   #set the variable "cars_driven" eqaul to the variable "drivers"
carpool_capacity = cars_driven * space_in_a_car         #set the variable "carpool_capacity" equal to product of the variable "cars_driven" and the variable "space_in_a_car"
average_passengers_per_car = passengers / cars_driven   #set the variable "average_passengers_per_car" equal to the quotient of the variable "passengers" and the variable "cars_driven"

print "There are", cars, "cars available."                                  #print out how many cars are available
print "There are only",  drivers, "drivers available"                       #print out how many drivers are available
print "There will be", cars_not_driven, "empty cars today."                 #print out how many cars are empty today
print "We can transport", carpool_capacity, "people today."                 #print out how many people can transported today
print "We have", passengers, "to carpool today."                            #print out how many passengers are today in the carpool
print "We need to put about", average_passengers_per_car, "in each car."    #print out how many passengers are in each car
