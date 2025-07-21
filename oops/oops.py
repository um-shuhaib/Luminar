'''                              OOPS '''
# related fun and op wrapped together and structure - remove unwanted operations
# object, class, methods
# methods - function 

class Mobile:
    def calling(self):         # refering the current obj
        print("calling...")
    
Mobile.calling()
# or
Mobile1=Mobile()   # obj created  ''' when using obj an ref numbewr is sent as argument '''
Mobile1.calling() # there will be an error or for fix set an parameter in the class