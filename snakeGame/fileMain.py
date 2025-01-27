# using with automatically closes the file after reading
#with open("my_text.txt") as file:
#    contents = file.read()
#    print(contents)


#with open("my_text.txt", mode="a") as file:
#    file.write("\nNew text.")


#with open("new_file.txt", mode="w") as file:
#   file.write("New file.")

with open("/Users/kunalshenoy/Documents/GitHub/HundredDaysOfPython/snakeGame/my_text.txt") as file:
    contents = file.read()
    print(contents)