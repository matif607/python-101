def multiply(n1, n2):
    result = n1 * n2
    return result


# for val in range(1, 6):
#     two_times = multiply(2, val)
#     print(two_times)


def is_palindrome(string):
    # backwards = string[::-1]
    # return  backwards == string
    # return string[::-1].lower() == string.lower()
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    sentence = ''
    for char in string:
        if char.isalnum():
            sentence += char
    return is_palindrome(sentence)


def fibonacci(n):
    """Return the `n`th fibonacci number for positive `n`"""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n -1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))


# word = input("Please enter a sentence to check if it is a palindrome: ")
#
# if palindrome_sentence(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

