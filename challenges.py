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



#Create a function that accepts an input and determines all factors of a number



    
