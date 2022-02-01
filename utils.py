def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    print(maximum)   #instead of this we can use return too....    like return


