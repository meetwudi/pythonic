# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
perm_list = map(lambda x: int(x), raw_input().split(' '))
perm_dict = {}
for idx, val in enumerate(perm_list):
    perm_dict[idx+1] = val
result = [perm_dict[x] for x in perm_list]

for x in result:
    print x
