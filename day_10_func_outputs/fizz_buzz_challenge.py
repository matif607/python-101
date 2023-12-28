def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz
    :param number: The number to check
    :return: `fizz` if the number is divisible by 3
        `buzz` if the number is divisible by 5
        `fizzbuzz` if the number is divisible by 3 and 5
        the number as string if otherwise
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


correct_answer = []

is_answer_correct = True

