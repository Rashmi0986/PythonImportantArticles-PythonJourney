def get_takoballs(orders):
  for order in orders:
    yield f'{order} takoballs'

for food in get_takoballs([4, 6, 8]):
  print(food)

# return adds to delay where in yield is much faster in memory terms .
# yield vs return with example - https://levelup.gitconnected.com/return-vs-yield-in-python-a-short-comic-f714465a0e92