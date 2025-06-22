# function with return statement
def add(a, b):
    return a+b


result = add(2, 5)  # method 1 to print returned value
print(result)
print(add(2, 5))  # method 2 to print returned value


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()  # title() fumction is used to format strings
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name('SANJANA', 'kanavi'))
