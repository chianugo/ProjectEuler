""""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""


def findSum(limit, number1, number2):
    currentSum = 0
    for i in range(limit):
        if (i % number1 == 0) or (i % number2 == 0):
            currentSum += i
        """if i % (number1 * number1) == 0:
            currentSum -= i"""
    return currentSum


print(findSum(1000, 3, 5))
