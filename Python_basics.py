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
