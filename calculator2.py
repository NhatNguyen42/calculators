import time
def add(var1,var2):
	return var1 + var2
def minus(var1,var2):
	return var1 - var2
def times(var1,var2):
	return var1 * var2
def divide(var1,var2):
	try:
		return var1 / var2
	except ZeroDivisionError:
		print("divide by zero error, returning zero")
		return 0

def runOperation(operation, var1, var2):
	if(operation == 1):
		print(add(var1, var2))
	elif(operation == 2):
		print(minus(var1, var2))
	elif(operation == 3):
		print(times(var1, var2))
	elif(operation == 4):
		print(divide(var1, var2))
	else:
		print("no operation assigned to that number, try again.")

	

def main():
	
	validinput = False
	while not validinput:
		try:
			var1 = int(input("insert first number here:  "))
			var2 = int(input("insert second number here:  "))
			operation = int(input("what do you want to do? (1:add, 2:minus, 3:times, 4:divide):  ") )
			validinput = True
			print("calculating")
			time.sleep(0.000000000000001)
		except ValueError:
				print("invalid input, try again.")
				main()
		except:
			print("unknown error")
		runOperation(operation, var1, var2)
		main()
		
main()

