# set comprehension
estherset = {letter.upper()
             for letter in "Esther Lee is the only one I love"}
print 'estherset: ', estherset

johnset = {letter.upper()
           for letter in 'John love Esther'}
print 'johnset: ', johnset

# set operations
print 'intersection: ', johnset & estherset
print 'diff: ', johnset ^ estherset
print 'substract: ', johnset - estherset
