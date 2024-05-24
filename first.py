#first.py
from datetime import date
sum = 1 + 2 
print(sum)
product = sum * 2 
print (product)

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print("planets_in_solar_system is of type - ", type(planets_in_solar_system))
print("distance_to_alpha_centauri is of type - ", type(distance_to_alpha_centauri))
print("can_liftoff is of type - ", type(can_liftoff))
print("shuttle_landed_on_the_moon is of type - ", type(shuttle_landed_on_the_moon))


print(date.today())
print("Today's date is = ", date.today())
print("Date is of type - ", type(date))
#To make this code work, you need to convert the date into a string. 
#You accomplish such a conversion by using the utility function str():
print("Today's date is " + str(date.today()))