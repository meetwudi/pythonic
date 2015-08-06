# part 1 - with no argument
def wrapper(func):
  def inner():
    print 'before calling function'
    result = func()
    print 'after calling function'
    return result
  return inner

@wrapper
def great():
  print 'this is great'

great()

# part 2 - with arbitrary arguments
def wrapper2(func):
  def inner(*args, **kwargs):
    print 'number of arguments (*args): ', len(args)
    print 'number of keyword arguments (**kwargs)', len(kwargs.keys())
    return func(*args, **kwargs)
  return inner

@wrapper2
def great2(*args, **kwargs):
  return sum(args)

print great2(1, 2, 3)
