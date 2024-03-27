import os
import argparse

def print_tree(directory, prefix='', extensions=None):
    """
    Print the directory tree structure. Only include files matching the given extensions.
    """
    # Sort directory contents by name
    entries = sorted(os.listdir(directory))
    filtered_entries = [e for e in entries if os.path.isdir(os.path.join(directory, e)) or
                        any(e.endswith('.' + ext) for ext in extensions)] if extensions else entries
    
    for i, entry in enumerate(filtered_entries):
        path = os.path.join(directory, entry)
        is_last = i == (len(filtered_entries) - 1)
        marker = '└── ' if is_last else '├── '
        print(prefix + marker + entry)
        if os.path.isdir(path):
            extend_prefix = '    ' if is_last else '│   '
            print_tree(path, prefix=prefix+extend_prefix, extensions=extensions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Visualize directory structure with optional file extension filtering.")
    parser.add_argument('directory', nargs='?', default=os.getcwd(), help="Directory path to visualize.")
    parser.add_argument('-e', '--extensions', help="Comma-separated list of file extensions to include (e.g., tsx,ts,js).", default='')
    args = parser.parse_args()

    # Prepare extensions list
    extensions = args.extensions.split(',') if args.extensions else []

    print(args.directory)
    print_tree(args.directory, extensions=extensions)
