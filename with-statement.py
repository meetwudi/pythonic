class controlled_execution:
    def __enter__(self):
        print 'enter'
        return {'this': 'is awesome'}
    def __exit__(self, type, value, traceback):
        print 'exit'

with controlled_execution() as obj:
    print 'working'
