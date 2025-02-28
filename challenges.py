""" # Let's create a function that determines if a number is odd or even
def odd_even(x):
    if x % 2 == 0: 
        print("even")
    else:
        print("odd")
odd_even(9) """



""" #Lets create a function to accept a "bill" value and offer a tip of 0%, 15%, 20%, or 25% depending on if the service is bad, okay, good, or great
def calculate_total(bill_amount):
    service = input("How was the service")
    if service == "bad":
        total = bill_amount * 1.0
    if service == "okay":
        total = bill_amount * 1.15
    if service == "good":
        total = bill_amount * 1.20
    if service == "great":
        total = bill_amount * 1.25
    print(total)
calculate_total(100) """



""" #Create a function that accepts an input and determines all factors of a number
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    print(factors)
find_factors(10)
 """


#Create a function that accepts 2 arguments. Find the greatest common factor between those numbers
def find_factors(number1, number2):
    factors = []
    for i in range(1, number1 + 1):
        if number1 % i and number2 % i == 0:
                factors.append(i)
        print(factors)
    find_factors(56,98)
