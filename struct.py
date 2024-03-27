import os
import sys
import argparse

def print_tree(directory, prefix='', extensions=None):
    """
    Print the directory tree structure for files matching the given extensions.
    """
    files = sorted(os.listdir(directory))
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        if extensions and not file.split('.')[-1] in extensions:
            continue  # Skip files not in the specified extensions
        is_last = i == (len(files) - 1) - sum(not file.split('.')[-1] in extensions for file in files[i:])
        print(prefix + ('└── ' if is_last else '├── ') + file)
        if os.path.isdir(path):
            extend_prefix = '    ' if is_last else '│   '
            print_tree(path, prefix=prefix+extend_prefix, extensions=extensions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize directory structure with optional file extension filtering.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(), help='Directory path to visualize')
    parser.add_argument('-e', '--extensions', help='Comma-separated list of file extensions to include (e.g., tsx,ts,js)', default=None)
    args = parser.parse_args()

    # Split extensions into a list if provided
    extensions = args.extensions.split(',') if args.extensions else None
    
    print(args.directory)
    print_tree(args.directory, extensions=extensions)
