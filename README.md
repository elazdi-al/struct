# Directory Structure Visualizer

The Directory Structure Visualizer is a Python script that generates a tree-like representation of the structure of a specified directory or the current working directory if no directory is specified, detailing all its subfolders and files. This tool is invaluable for visualizing the layout of projects directly from the terminal, offering insights into the organizational structure at a glance.

## Features

- Generates a tree-like structure of a directory or the current working directory if no argument is given.
- Easy to use from the terminal, enhancing productivity and project understanding.
- Compatible across Linux, macOS, and Windows platforms.

## Installation

1. **Clone or Download the Script**
   - Obtain the script by cloning this repository or downloading the `main.py` file directly.

2. **Make the Script Executable**
   - **Linux/macOS**: Run `chmod +x main.py` in your terminal to make the script executable.
   - **Windows**: Python scripts are executable by default; no additional action is needed.

## Usage

To use the Directory Structure Visualizer, follow these steps depending on your operating system:

### Linux and macOS

1. **Direct Execution**
   - Navigate to the directory where `main.py` is located and execute using `./main.py` or `./main.py /path/to/directory` to specify a directory.
   
2. **Terminal Command**
   - **Create an Alias**: Add `alias struct='/absolute/path/to/main.py'` to your `.bashrc` or `.zshrc` file for global access.
   - **Or Move to BIN**: For even easier access, move the `main.py` to `/usr/local/bin` and rename it to `struct`.

### Windows

1. **Command Line Execution**
   - Open Command Prompt or PowerShell, navigate to the script's location, and run `python main.py` or `python maint.py \path\to\directory`.

2. **Global Access**
   - Add the script's directory to your system's PATH environment variable and optionally rename `main.py` to `struct`, allowing it to be executed from any location.

## Example

```bash
$ struct
