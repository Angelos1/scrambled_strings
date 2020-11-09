import sys

def read_file(file_path):
    try:
        file = open(file_path, 'r')
        words = file.read().splitlines()
        file.close()
        return words
    except FileNotFoundError:
        print('File not Found: "' + file_path +'"' )
        sys.exit()
