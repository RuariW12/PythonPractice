# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1(): # variable a is local to func1
    a = 1
    print(a)

def func2(): # variable b is local to function 2
    b = 2
    print(b)

func1()
func2()

print()

def func3(): #able to use variable x in multiple functions because local
    x = 1
    print(x)

def func4():
    x = 2
    print(x)

func3()
func4()

print()


#ENCLOSED

def func5(): #functions inside of functions have "order of operations" when it comes to claiming what a variable will value
    x = 1

    def func6():
        x = 2 # if this line is removed then when printing x it will assume function 5
        print(x)
    func6()

func5()

#GLOBAL

x = 3 #global variable, less important than local and enclosed






