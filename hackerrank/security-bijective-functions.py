n = int(raw_input())
list_of_numbers = raw_input().split(' ')
set_of_numbers = set(list_of_numbers)
result = True if len(list_of_numbers) == len(set_of_numbers) else False

if result:
    print 'YES'
else:
    print 'NO'
