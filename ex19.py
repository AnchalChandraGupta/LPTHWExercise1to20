#Ex19 Write at least one more function of your own design, and run it 10 different ways.

def abc(x, y, z, p):
    print "You have %d %s" % (x,z)
    print "You have %d %s" % (y,p)
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

for i in range (1,11):
    print(i)
    abc(i, 7+i, " apple", "abc")

