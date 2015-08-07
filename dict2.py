# looping through dict using dict.iteritems
dict = {
    'Esther Lee': 'sweet',
    'John Wu': 'good',
}

# not in order though
# should not rely on that
for k, v in dict.iteritems():
    print k, 'is', v
