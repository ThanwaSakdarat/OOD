from distutils.command import bdist_dumb
from hashlib import new
from types import new_class

input_string = input("Enter All Bid : ").split()

if len(input_string)<2:
    print('not enough bidder')

new_class = []
for i in input_string:
    new_class.append(int(i))

new_class.sort(reverse=True)
if new_class[0] == new_class[1]:
    print('error : have more than one highest bid')
else:
    print('winner bid is ' + str(new_class[0]) + ' need to pay ' + str(new_class[1]))