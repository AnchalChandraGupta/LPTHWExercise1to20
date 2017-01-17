#Ex13.02 Write a script that has fewer arguments and one that has more in the unpacked variables.

inputlist = [1,2,3,4];

script, first, second, third = inputlist

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#inputlist = [1,2,3,4,5];
# Traceback (most recent call last):
#   File "/home/hanshika/PycharmProjects/Project1/apple.py", line 3, in <module>
#     script, first, second, third = inputlist
# ValueError: too many values to unpack
#
#inputlist = [1,2,3];
# Traceback (most recent call last):
#   File "/home/hanshika/PycharmProjects/Project1/apple.py", line 3, in <module>
#     script, first, second, third = inputlist
# ValueError: need more than 3 values to unpack

