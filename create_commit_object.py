import sys
import argparse
import time
import os
import utils

def seconds_since_epoch():
    return int(time.mktime(time.localtime()))

parser = argparse.ArgumentParser()
parser.add_argument("--tree-id", help="SHA1 of the tree object to commit", required=True)
parser.add_argument("--name", help="Name of the author/commiter", required=True)
parser.add_argument("--email", help="Email of the author/commiter", required=True)
parser.add_argument("--msg", help="Commit message", required=True)
namespace = parser.parse_args()

tree_id = namespace.tree_id
name = namespace.name
msg = namespace.msg
email = namespace.email
time = seconds_since_epoch()
timezone="+0200"

tree_line = "tree {}\n".format(tree_id)
identity_line = "{} <{}> {} {}\n".format(name, email, time, timezone)
author_line = "author " + identity_line
commiter_line = "commiter " + identity_line

contents = tree_line + author_line + commiter_line + "\n" + msg
contents = "commit {}\x00".format(len(contents)) + contents

utils.write_git_object(contents.encode())
