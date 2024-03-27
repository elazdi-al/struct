import os
import sys

def print_tree(directory, prefix=''):
    """
    Print the directory tree structure.
    """
    files = sorted(os.listdir(directory))
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = i == (len(files) - 1)
        print(prefix + ('└── ' if is_last else '├── ') + file)
        if os.path.isdir(path):
            extend_prefix = '    ' if is_last else '│   '
            print_tree(path, prefix=prefix+extend_prefix)

if __name__ == '__main__':
    root_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    print(root_directory)
    print_tree(root_directory)
