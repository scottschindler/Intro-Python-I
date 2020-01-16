"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(str(sys.argv))


# Print out the OS platform you're using:
# YOUR CODE HERE

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
print(os.name)

# Print the current process ID
# YOUR CODE HERE
print (os.getpid())

# Print the current working directory (cwd):
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

# Print out your machine's login name
# YOUR CODE HERE

import getpass
username = getpass.getuser()
print(username)


# come back to this one to correct for potentially incorrect ones. 