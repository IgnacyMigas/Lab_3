#!/usr/bin/pyhon2.7.9

class notANumber(Exception):
	def __str__(self):
		return repr("Argument is not float or int")

class divByZero(Exception):
	def __str__(self):
		return repr("Division by zero")

class isNegative(Exception):
	def __str__(self):
		return repr("Argument is negative number")

class notFunction(Exception):
	def __str__(self):
		return repr("Argument 1 is not a function")
