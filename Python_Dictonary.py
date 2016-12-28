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