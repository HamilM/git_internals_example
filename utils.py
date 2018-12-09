import os
import hashlib
import zlib

def append_sep_if_needed(path):
    if path.endswith(os.path.sep):
        return path
    return path+os.path.sep

def get_parent_of_path(path):
    path = append_sep_if_needed(path)
    return os.path.realpath(path+os.path.pardir)

def get_path_of_git_dir(from_path):
    while True:
        from_path = append_sep_if_needed(from_path)
        check_dir = from_path + ".git" + os.path.sep
        if os.path.exists(check_dir):
            return check_dir
        parent = get_parent_of_path(from_path)
        if parent == from_path:
            return None
        from_path = parent 

def write_git_object(contents):
    # Find git dir
    git_dir = get_path_of_git_dir(os.getcwd())
    if None == git_dir:
        print("No .git dir found! leaving...")
        sys.exit(-1)

    # Generate hash for the final contents
    hash_value = hashlib.sha1(contents).hexdigest()
    dir = git_dir + "objects" + os.path.sep + hash_value[0:2] + os.path.sep
    object_name = hash_value[2:]

    # Create the directory
    try:
        os.mkdir(dir)
    except OSError:
        # If the directory already exists...
        pass

    # Write the final content
    with open(dir + object_name, 'wb') as f :
        compressed_contents = zlib.compress(contents)
        f.write(compressed_contents)
    print(hash_value)
