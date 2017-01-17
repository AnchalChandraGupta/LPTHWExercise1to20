#Ex11.3. Write another "form" like this to ask some other questions.
print "Enter your name:",
firstName = raw_input()
print "Enter middle name:",
middleName = raw_input()
print "Enter last name:",
lastName = raw_input()

print "Your \nfirst name: %r \nmiddle name: %r\nlast name: %r" % (
    firstName, middleName, lastName)
