###################################################################################
 #Functions

def func_name(param1,param2):
	print "something goes on \n"
	something =7
	return something,param2,param1

x=func_name(5,6)
print x

def sumandiff(num1,num2):
	return num1+num2,num1-num2

print sumandiff(6,5)	

#Create a list using functions
def mklist():
	l=[];
	while True:
		a=raw_input("Enter elements\n")
		if not a:
			break;
		a=int(a)	
		l.append(a)
	#print l
	return l

l=mklist()
print l


#Write a function to create a list and sum all even numbers it with other function
def mklist():
	l=[];
	while True:
		a=raw_input("Enter elements\n")
		if not a:
			break;
		a=int(a)	
		l.append(a)
	#print l
	return l
def sumlist():
	#print ul
	temp=0
	for e in l:
		if (e%2)==0:
			temp=temp+e			
	return temp

l=mklist()
print l
temp= sumlist()
print temp


#Create a list which reads number as string an converts it to integer using function
#Create another function to add these numbers

def create_list():
	l=[]
	
	p=[]
	var=0
	while True:
		data=raw_input("Enter Numbers")
		if not data:
			break;
		p=data.split()
		s=[]
		for i in p:
			var=int(i)
			s.append(var)
		l.append(s)
	return l


def addition():
	val=0
	for e in l:
		for i in e:
			val=val+i
	return val

l=create_list()
print l
 
val=addition()
print val

#print pattern
1
1 2
1 2 3   so on 

def mklist():
	l=[];
	while True:
		data=raw_input('Enter list elemsnts');
		if not data:
			break;
		data=int(data)
		l.append(data)
		
	return l
def pattern():
	
	print l
	s=[]
	for i in l:
		s.append(i)
		print s
	return s
		

l=mklist()
s=pattern()

#Named Argument:

def morefun(age,name='none'):
	print name,age

morefun(name='pm',age='99')


Default argument
def fun(name='None'):
	print name
fun()
fun('prithvi')


#Named argument

def fun(name,gender,age):
	s='Mr {name},{gender} with age of {age}'
	print s.format(name=name,gender=gender,age=age)
fun('prithvi','male','22')



def fun(age,gender,name):
	s='Mr {name},{gender} with age of {age}'
	print s.format(name=name,gender=gender,age=age)
fun('22','male','prithvi')

	
#Generate a Tree Pattern

def printCenter(width,stars):
    print stars.center(width,' ')

def getstar(width,rowNum=0):
    stars =  rowNum * '*' + (rowNum-1) * '*'
    printCenter(width,stars)

def generateTree(h):
    width = 2 * h -1
    for i in range(h):
        getstar(width,i+1)

h = int(raw_input("Height : "))
generateTree(h)



#Separate string and interger from a list
l=['1','2','3','4','5','s','6','p']
# print type(l[0])
print l
i=0
s=[]
p=[]

for i in l:
	try:
		s.append(int(i))
	except:
		p.append(i)
		pass		
print s
print p 