# dailyprogrammer easy challenge 1

# prompt user for information to type in
name = raw_input("What is your name? ")
age = raw_input("How old are you? ")
username = raw_input("What's your reddit username? ")

# log info to the console
print "Your name is %s, you are %s years old, and your username is %s." % (name, age, username)

# create file in current directory
# or open and append to file if it already exists
file = open("reddit-peeps.txt", 'a')

# save the parameters
s = "%s, %s, %s\n" % (name, age, username)

# write them to the file and close it
file.write(s)
file.close()