def intro(name):
    print("Hello, my name is ", name)

user_name = "Ranveer Jaiswal"
intro(user_name)



def recur_factorial(n):
    if n ==1:
       return n 

    else:
        return n*recur_factorial(n-1)


num = 7

if num < 0:
    print("0 cannot have a factorial")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    print("The factor of ", num , "is" , recur_factorial(num))





def sum(x,y):
    return x + y

def subtract(x,y):
    return x - y

def product(x,y):
    return x * y

def divide(x,y):
    return x / y


num1 = 74
num2 = 29

print("The sum is:",sum(num1,num2))
print("The difference is" ,subtract(num1,num2))
print("The product ofis" ,product(num1,num2))
print("The quotion is" ,divide(num1,num2))