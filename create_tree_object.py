import utils
import os
import sys
import base64
lines = sys.stdin.buffer.readlines()
tree_entries = []

# Generates a single tree object entry
def generate_line_from_input_line(input_line):
    mode,name,sha=input_line.decode().split(",")
    sha=sha.strip()
    mode=mode.strip()
    name=name.strip()
    return mode.encode() + b" " + name.encode()+ b"\x00" + base64.b16decode(sha, True)

for l in lines:
    tree_entries.append(generate_line_from_input_line(l))
contents = b''.join(tree_entries)

# Generate the header of the tree object
contents = b"tree "+str(len(contents)).encode() + b"\x00" + contents

utils.write_git_object(contents)
