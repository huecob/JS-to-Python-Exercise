"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for elements in items:
        print(elements)
output_all_items([1, 'hello', True])

def get_all_evens(nums):
    retval = []
    for elements in nums:
        if elements % 2 == 0:
            retval.append(elements)
    return retval


def get_odd_indices(items):
    retval = []
    for i in range(len(items)):
        if i % 2 == 1:
            retval.append(items[i])
    return retval

def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    nums = []
    for i in range(start,stop):
        nums.append(i)
    return nums


def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []
    converted_value = string.split('_')

    for word in converted_value:
        camel_case.append(word[0].upper() + word[1:])
    return ''.join(camel_case)


def longest_word_length(words):
    longest_word = words[0]

    for elements in words:
        if len(elements) > len(longest_word):
            longest_word = elements
    return len(longest_word)


def truncate(string):
    retval = []
    #loop over string
    for letters in string:
    #add characters into an accumulator
        if letters not in retval:
            retval.append(letters)
        else:
            continue

    return ''.join(retval)
    #if that character exists, skip it
    #return the string


def has_balanced_parens(string):
    #iterate through the string, count how many () there are of each
    right_side = 0
    left_side = 0
    for target in string:
        if target == '(':
            left_side += 1
        elif target == ')':
            right_side +=1

    if right_side == left_side:
        return True
    else:
        return False
    


def compress(string):
    compressed = []

    currChar = ''
    charCount = 0
    for char in string:
        if char != currChar:
            compressed.append(currChar)

            if charCount > 1:
                compressed.append(str(charCount))

            currChar = char
            charCount = 0

        charCount += 1

    compressed.append(currChar)
    if charCount > 1:
        compressed.append(str(charCount))

    return ''.join(compressed)
