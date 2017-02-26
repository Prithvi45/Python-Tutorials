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