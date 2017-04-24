import string

p1 = "BigBird21"
p2 = "boring_password!"

# output: True if password meets mimimum threshold, False otherwise
def pwChecker(password):
	upper = [True if x.isupper() else False for x in password]
	lower = [True if x.islower() else False for x in password]
	digit = [True if x.isdigit() else False for x in password]
	return True in upper and True in lower and True in digit

#output: a float on a scale of 1-10
def pwRating(password):
	nonAlpha = ".?!&#,;:-_*"
	rating = 0.0
	if pwChecker(password):
		rating += 5.0
	if len(password) > 8:
		rating += 1.0
	bonus = [
		4.0 / len(password) if x in nonAlpha
		else 0.0
		for x in password
	]
	for x in bonus:
		rating += x
	return rating

print "pwChecker(BigBird21):\t" + str(pwChecker(p1)) + "\n"
print "pwChecker(boring_password!):\t" + str(pwChecker(p2)) + "\n"
print "pwRating(BigBird21):\t" + str(pwRating(p1)) + "\n"
print "pwRating(boring_password!):\t" + str(pwRating(p2)) + "\n"
