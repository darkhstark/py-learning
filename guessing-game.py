import random 

print ("Enter a range of numbers: ")
start = int (input ("Starting number: " ))
end = int (input ("ending number: "))

print (start, end)

print ("You have 3 attempts to guess the number: ")

for i in range(3):
	find = int (input ("Make your guess: " ))
	rnd = random.randrange(start, end) 
	print (rnd)
	if rnd == find:
		print ("You guessed right")
		break
	else:
		print ("try again loser!") 
