# Enter your code here. Read input from STDIN. Print output to STDOUT

y_to_x_map = {}

n = int(raw_input())
y_list = map(lambda x: int(x), raw_input().split(' '))
for x, y in enumerate(y_list):
    y_to_x_map[y] = x + 1
for y in xrange(1, n + 1):
    print y_to_x_map[y]
