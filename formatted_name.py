# def format_name(f_name,l_name):
#     return f_name+" "+l_name

# first_name = input("Enter your first name:\n").capitalize()
# last_name = input("Enter your last name:\n").capitalize()

# complete_name = format_name(first_name,last_name)
# print(f"Hello {complete_name}")

#Doing the same by another method

def formatted_name(f_name,l_name):
    #an example of docstring
    """Take a First and a last name and format it to return the title case version of the name"""
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Hello {formatted_f_name} {formatted_l_name}"

print(formatted_name.__doc__)
print(formatted_name(f_name=input("Your First Name:\n"),l_name=input("Your Last Name:\n")))
#it's not a new concept, you've already been using it (remember the len() function)
#print(len('Angela'))