#Ex14.02 Change the prompt variable to something else entirely.
from sys import api_version
print(api_version)
inputList = ['A','B']
script, user_name = inputList
prompt = '>>> '

print "Name %s, Scr %s." % (user_name, script)
print "I'd like to ask you a few questions."
print "abcd Enter input: "
likes = raw_input(prompt)

print "efgh Enter input: "
lives = raw_input(prompt)

print "ijkl Enter input: "
computer = raw_input(prompt)

print """  Entered input: %s   %s    %s
""" % (likes, lives, computer)
