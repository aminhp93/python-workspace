def difference(a, b):
  return [item for item in a if item not in make_set(b)]

def make_set(itr):
  print('Making set...')
  return set(itr)

print(difference([1, 2, 3], [1, 2, 4]))
# Making set...
# Making set...
# Making set...
# [3]