# 2. to check if the given string is palindrome or not

word = input('enter a word to check for palidrome: ')

reversed_word = word[::-1]

if word == reversed_word:
    print(f'the given word {word} is palindrome')
else:
    print(f'the given word {word} is not palindrome')

# 3. Input a sentence or a paragraph from user and extract how many unique words are used and display the count

sentence = input('enter your sentence or paragraph: ')

wordsSplit = sentence.split(' ')
print(wordsSplit)

uniqueWords = set()

for individualWord in wordsSplit:
    uniqueWords.add(individualWord)

uniqueCount = len(uniqueWords)

print(f'the total number of unique terms are: {uniqueCount}')


# 4. Create a dictionary with a person's name and contact info for a small company, take the input from a user to search for a user using their name, return the number (example user will search for 'Ram' and if user exists, their phone number is returned)

employeeDictionary = {
    'Ram': 9866787383, 'Sita': 78074082348, 'Hari': 98097248
}

nameToBeSearched = input('enter the name whose phone number you want: ')
capitalizedName = nameToBeSearched.capitalize()
if(capitalizedName in employeeDictionary):
    print(f'the phone number of {capitalizedName} is {employeeDictionary[capitalizedName]}')
else:
    print(f'user {capitalizedName} not found')



# 1. Take input from user for two words, and check if they are anagrams (anagram example: listen and silent -> both contain the same number and set of alphabets)

firstWord = input('Enter a word: ')
secondWord = input('Enter another word to check: ')

sortedFirstWord = sorted(list(firstWord))
sortedSecondWord = sorted(list(secondWord))

if sortedFirstWord == sortedSecondWord:
    print(f'the given words {firstWord} and {secondWord} are anagrams.')
else:
    print(f'the given words {firstWord} and {secondWord} are not anagrams')