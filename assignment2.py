# # 1. Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence. Use both Recursion and regular method

# #regular method

# number = int(input('Enter any number: '))
# a,b = 0,1
# for i in range(number):
#     print(a, end = ",")
#     a,b = b, a+b 


# #using recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Print first n Fibonacci numbers
# num = int(input("Enter how many terms: "))
# for i in range(num):
#     print(fibonacci(i), end=", ")


# # 2. Accept a word/sentence from the user and count how many vowels (a, e, i, o, u) are present in it.
# word = input('\n enter a word: ')
# count = 0
# for letter in word:
#     if letter.lower() in ['a','e','i','o','u']:
#         count+=1
# print(f'the number of vowels present in {word} is {count}')


# # 3. Read a text file and count the number of words in it. Handle the case where the file might not exist.
# def count_words_in_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read()
#             words = text.split()
#             word_count = len(words)
#             print(f"Total number of words: {word_count}")
#     except FileNotFoundError as e:
#         print(e)

# Example usage
count_words_in_file('text-file.txt')