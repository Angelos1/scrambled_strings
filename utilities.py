
def read_file(file_path):
    file = open(file_path, 'r')
    # words = file.readlines()
    words = file.read().splitlines()
    file.close()
    return words

# dictionary_list("Files/dictionary1")