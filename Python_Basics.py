###Python Basics

#1. Find the Greatest Number
i=20
j=30

if i>30:
    print "i is greater than j"
else:
    print "j is greater then i"


#2 Print 1 to 9 Numbers using while
i=1
while i<10:
  print i
  i=i+1

#3 Print 1 to 9 Numbers using Infinite While loop
i=1
while True:
  print i
  i+=1
  if i==10:
      break

#4. Print all even number from 1 to 100
i=1
while i<100:
  if (i%2)==0:
      print i
  i+=1

#5 Print all the numbers which are divisible by 3 or 5 
i=1
while i<100:
  if (i%5)==0 or (i%3)==0:
      print i
  i+=1


l=[10,20,30,40,50,60]
for e in l[:5]:
	print e


#6. print all characters from string
s="i love india"
for i in s:
	print i


#7. Print ovels from below string 
for ch in "india":
  if ch in 'aeiou':
    print ch


#8. Read the number and check it is a positive ornegative number
num = float(raw_input("Enter a number: "))
if num > 0:
    print("Positive number")


print("This is always printed")

#9. Print all odd number from a list
l=[1,2,3,4,5,6,7,8,9]
for i in l:	
  if i%2!=0:
      print i

#10. Print the numbers which are divisible by 5
i=1
while i <100:
	i+=1
	if i%5==0:
		print i

#11 . Reverse the Below sentence 
"i love india"   as "india love i"

print ("Enter the String");
str=str(raw_input());
l=str.split();
n=l[::-1]
print n
m=' '.join(n)
print m


#12. print the string which starts with 'a' 
words=['abc','defe','acd','bhj']
print words 
for i in words:
	if i.startswith('a'):
		print i



#13. Sort the below list in descending order 
l=[1,2,3,4]
if len(l) > 2:
  l.sort()
  l.reverse()
  print l[0:len(l)]
else:
  print l



#14.Program: print the string who has even number of characters
pm=['h','hi','hello','hhhhhh','hellohello']
print pm
for i in pm:
	if (len(i)%2==0):
 		print i
output:
['h', 'hi', 'hello', 'hhhhhh', 'hellohello']
hi
hhhhhh
hellohello
[Finished in 0.0s]



#15.Program: print string  strating with 'a'
p=['hii','abc','acb']
print p
for i in p:
    if i.startswith('a'):
        print i

output:
['hii', 'abc', 'acb']
abc
acb
[Finished in 0.0s]


#16.Program : replcae z from all string with '<space>'

pm=['abz','abc','azz','azd'];
print pm
l=[];
for i in pm:
	t=i.replace('z',' ')
	l.append(t);
print l

output:
['abz', 'abc', 'azz', 'azd']
['ab ', 'abc', 'a  ', 'a d']
[Finished in 0.0s]




#17.Program: Take five numbers from user and store in the list 
l=[]
while True:
	number=raw_input("Enter Number:- ")
	if not number:
		break
	l.append(int(number))
	
print l



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





###################################################################################
#Dictonary

#Create an Empty Dictonary
db={}
print db

#create a dictonary which contains name as key and age as value
db={}
db={'prithvi':22,'awi':25}
print db


#create a Dictonary 'key' as name and value as age and print key and values
db={}
while True:
	name=raw_input("Enter your Name:")
	if not name:
		break;
	age=raw_input("Enter Your Age")
	db[name]=int(age)

for keys,values in db.items():
	print "Name: ",keys 
	print "Age: ",values



#create a Dictonary 'key' as name and value as age using function
def dictfun():
	db={}
	while True:
		name=raw_input("Enter name")
		if not name:
			break;
		age=int(raw_input("Enter age"))
		db[name]=age
	return db

mydb=dictfun()

print mydb

for k,v in mydb.items():
	print 'keys : ',k
	print 'values : ',v

	
#print who's age is < 18 from above code
def dictfun():
	db={}
	while True:
		name=raw_input("Enter name")
		if not name:
			break;
		age=int(raw_input("Enter age"))
		db[name]=age
	return db
mydb=dictfun()
print mydb
s=[]
for k,v in mydb.items():
	if v <18:
		s.append(k)
print s


#Create a dictionary with key as name and age as value and remove the the names from dictionary which have age < 18
def dictfun():
	db={}
	while True:
		name=raw_input("Enter name")
		if not name:
			break;
		age=int(raw_input("Enter age"))
		db[name]=age
	return db

mydb=dictfun()
print mydb

for k,v in mydb.items():
	if v <18:
		mydb.pop(k)

print mydb



#Create a dictonary which contains name as key and a list of dictonaries of subject and marks as a value

def dict():
	while True:
		s=[]
		db1={}
		
		name=raw_input("Enter your Name \n")
		if not name:
			break
		data=int(raw_input("enter Maths Marks "))
		db1['Maths']=data
		
		data1=int(raw_input("enter Science Marks"))
		db1['Science']=data1
		data2=int(raw_input("Enter English Marks"))
		db1['English']=data2
		s.append(db1)
		out[name]=s
	return out

out={}
mydb=dict()
print mydb
	

lists=dict()


#Create dictonary for purchase details: key as name and value as a dictionary of product and quantity 

def crdict():
	
	out={}
	while True:
		product={}
		name=raw_input("Enter customer Name : ")
		if not name:
			break;
		while True:			
			key=raw_input("Enter product name : ")
			if not key:
				break
			value=int(raw_input("Enter quantity :"))
			product[key]=value
			out[name]=product	
		
	return out

mydb=crdict()
# print mydb
for k,v in mydb.items():
	print ' Name : ',k
	print ' Purchase :',v
	




def crdict():
	db={}
	while True:
		s=[]
		name=raw_input("Enter Product Name")
		if not name:
			break
		while True:
			val=(raw_input("Enter Prices"))

			if not val:
				break
			val=int(val)
			s.append(val)
		db[name]=s
	return db

mydb=crdict()
print mydb
value=[]
for k,v in mydb.items():
	
	for i in v:
		value.append(i)
value.sort()
print value

#conversion of key to value nd vice versa
print db
newdb={}
for k,v in db.items():
	for e in v:
		if e not in newdb:
			newdb[e]=[k]
		else:
			newdb[e].append(k)


print newdb