programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

# An example dictionary
colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

#Will print "green"
print(colours["pear"])

#This is how you retrieve items from a dictionary:
colours["peach"] = "pink"

#This is how to create an empty dictionary:
my_empty_dictionary = {}

#This is how you can add new items to an existing dictionary:

colours["peach"] = "pink"

#This is also how you can edit an existing value in a dictionary:
colours["apple"] = "green"

#This is how to loop through a dictionary and print all the keys:
for key in colours:
    print(key)

#This is how to loop through a dictionary and print all the values:
for key in colours:
    print(colours[key])