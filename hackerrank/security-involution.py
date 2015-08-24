# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
perm_list = map(lambda x: int(x), raw_input().split(' '))
perm_dict = {}
for idx, val in enumerate(perm_list):
    perm_dict[idx+1] = val
result = [perm_dict[x] for x in perm_list]

if result == range(1, n + 1):
    print 'YES'
else:
    print 'NO'
