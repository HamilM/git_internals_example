import sys
import os
import utils

# Read the contents
contents = sys.stdin.buffer.read()

# Format the contents according to git blobl format
contents = "blob {}\0".format(len(contents)).encode() + contents

# Create the file
utils.write_git_object(contents)

