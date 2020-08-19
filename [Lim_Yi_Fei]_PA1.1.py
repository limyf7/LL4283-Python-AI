'''
10+3
Needlessly complicated conversions (you can more directly generate the result with list comprehensions), and the placeholders for the numbers can be more automatically generated.
'''
'''
# create list of results of the multiplication table 1x-10x
content = [x * y for x in range(1, 11) for y in range(1, 11)]

# add 1x, 2x, 3x etc. to every 10th element, after the first element in the content
i = 1
d = 0
while d < len(content):
    content.insert(d, str(i) + 'x')
    i += 1
    d += 11

# convert content into list of each row in table
row = [content[x:x + 11] for x in range(0, len(content), 11)]

# print all rows in table form
for item in row:
    print('{:<10} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}'.format(*item))

'''

for i in range(1,11):
  print("\n{:2d}x ".format(i))
  for j in range(1,11):
    print("{:<4d}".format(i*j))