# # Decorators


def myannotation(func):                    #Function sayHello is passed as an Argument
    print func
    def myWorld(arg):
        #pre conditions/ validations
        print 'Case'
        if arg == 'God':
            print  func(arg)
        return 'Good'
        
    return myWorld
    
    
@myannotation                        #Decorator
def sayHello(some):
    print 'Saying Hello ' + some
    
sayHello('Great')    #case 1

sayHello('God')    #case 2



# Decorators in Python 3
# def function():
#     print("hello word")
#
# func2 = function
# del function
# func2()

def dec1(func):
    def exec():
        print("execute now")
        func()
        print("executed")
    return exec

@dec1          # this is decorator 
def dec2():
    print("pv is good")

# pv = dec1(dec2)
dec2()
