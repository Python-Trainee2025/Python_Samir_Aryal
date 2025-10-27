help('keywords')


# naming convention
# for variables, use small case letters as variable_name
# for class names, use capitalized letters as ClassName

# if all caps naming convention used, it means that the value
# for that variable is constant

# example: PI=3.14 means constant, while pi=3.14 means varying value


# operators

number1= 5
number2= 2

mod = number1%number2

print(f'the modulus of the {number1} and {number2} is {mod}')


# comparison operators
a=5
b=5
if (a==b & b==a):
    print('both the numbers are equal')



name = "Samir"
greeting = 'Hello'

print(f'{greeting} there Mr.{name}')

reverse = name[::-1]
print(f'Reverse is {reverse}')



text = "Samir"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)


#commit test