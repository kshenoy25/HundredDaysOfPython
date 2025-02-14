# FileNotFound

#try:
#    file = open("a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    print("There was an error")
#    file = open("a_file.txt", "w")
#    file.write("Something")
#except KeyError as error_message:
#    print(f"The key {error_message} was not found.")
#else:
#    content = file.read()
#    print(content)
#finally:
#    raise TypeError("This is an error I made up")
    #file.close()
    #rint("The file was closed.")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

if height > 3:
    raise ValueError("Height is greater than 3 meters")

bmi = weight / (height * height)
print("Your BMI is", bmi)