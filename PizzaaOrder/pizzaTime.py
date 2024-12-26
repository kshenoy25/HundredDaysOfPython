print("Welcome to Pizza Time!")
size = int(input("What size pizza for you today? S M or L "))
pepperoni = input("Do you want pepporoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# customer pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size")

