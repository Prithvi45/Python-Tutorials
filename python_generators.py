
#Genarators
def gen():
	i = 0 
	while True:
		i+=1
		yield i



y = gen()
# Interators
print y.next()
print y.next()
print y.next()
print y.next()



#This can be implemented by using simple python fiunction as shown in below example
# polluting global space

# d = 0
# def oldfun():
#     global d
#     d += 1
#     return d

# print oldfun()
# print oldfun()


# But in this case we are polluting the global variables, everytime we r calling function






#Why generators ?

#Generators are performance focused
#Most of the python packages like itertools use this generators as below e.g 

# import itertools
# f = itertools.combinations(range(5),3)
# print f.next()
# print f.next()
