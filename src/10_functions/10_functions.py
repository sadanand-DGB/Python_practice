def goodDay():       #defining a function
    print("Good Day!")

goodDay()          #calling the function

#parameterized function
def goodDay(name):      #defining a function with parameter
    print("Good Day, " + name + "!")

goodDay("Sadanand")          #calling the function with argument

#example of function with default parameter
def goodDay(name, ending = "Thank you!"):      #defining a function with multiple parameters
    print("Good Day, " + name + "! " + ending)
          
goodDay("John", "Have a great day!")   #calling the function with both arguments
goodDay("Sadanand") #calling the function with only one argument, the default value for 'ending' will be used