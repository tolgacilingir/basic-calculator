def calc(x,y,ops):

	if ops not in "+-/*":
		return("Only +-/* !!!")

	if ops == "+":
		return(str(x) + " " + ops + " " + str(y) + "=" + str(x+y))
	elif ops == "-":
	    return(str(x) + " " + ops + " " + str(y) + "=" + str(x-y))
	elif ops == "*":
	    return(str(x) + " " + ops + " " + str(y) + "=" + str(x*y))    	
	elif ops == "/":
	    return(str(x) + " " + ops + " " + str(y) + "=" + str(x/y))   
while True:	    

	x = int(input("please enter first number: "))
	y = int(input("please enter second number: "))
	ops = str(input("Choose between x,-,*,/ "))

	print(calc(x,y,ops))
