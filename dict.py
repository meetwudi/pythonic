# enum over dict
dict = {
    'name': 'Esther Lee',
    'age': 21,
    'school': 'Tongji University'
}
print 'Resume'
for k in dict.keys():
    print k, ':', dict[k]
