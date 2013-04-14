import math

a = int(1.8)
b = int(32)
c = int(9)
d = int(5)
r = int(0)
again = "y"

while again == "y":
	
	 
	t = raw_input("Whats the Temperature? ")
	temp = int(t)

	u = raw_input("Whats the Unit? ")

	if u == "c":
		
		sfr1 = t * a
		sfr = int(sfr1)
		r = sfr + b  
	
	if u == "f":
		
		sfr1 = temp - b
		sfr = int(sfr1)
		tfr = sfr * d
		fft = int(tfr)
		r = fft / c
	
	if u == "celcius":
		
		sfr1 = t * a
		sfr = int(sfr1)
		r = sfr + b  
	
	if u == "fahrenheit":
		
		sfr1 = temp - b
		sfr = int(sfr1)
		tfr = sfr * d
		fft = int(tfr)
		r = fft / c

	print "Results: ", r
	again = raw_input("Type y to do another convert. Type n to quit. ")
	