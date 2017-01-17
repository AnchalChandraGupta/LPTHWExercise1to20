#Ex16.02, Write a script similar to the last exercise that uses read to read the file you just created.
# Open a file, write creates the file if it doesn't exist
fo = open("foo.txt", "wb")
fo.write( "Hello World!\nHello World!");

# Close opend file
fo.close()

fr = open('foo.txt')
content = fr.read();
print(content)
