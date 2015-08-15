try:
    f = open('data/data1.txt', 'r')
except (IOError):
    print str(IOError)
else:
    print 'Else'
