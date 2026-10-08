# Part one : Ask for todays temperature
Temperature = int(input("enter today's temperature in celsius : "))

# Part two decide to wear a t-shirt or a jacket
if Temperature < 20 :
   outfit = "jacket"
   print ("It is a cold day today.")
   print ("wear a", outfit)
else:
    outfit = "t-shirt"
    print ("it's a warm day today .")
    print ("wear a", outfit)
    
# Part three : Ask wether it is raining
