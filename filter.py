result = filter(lambda x: x % 3 == 0, xrange(10))
print result


def can_be_divided_by_3(num):
    return num % 3 == 0

result = filter(can_be_divided_by_3, xrange(10))
print result
