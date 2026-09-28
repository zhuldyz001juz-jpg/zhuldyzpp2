def count_up_to(n):
    number = 1

    while number <= n:
        yield number
        number += 1


for number in count_up_to(5):
    print(number)