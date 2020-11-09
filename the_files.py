import utilities as u
import sys

''' This class is for parsing the files into python lists'''
class TheFiles:
    def __init__(self, opts):
        for opt, arg in opts:
            if opt == "--dictionary":
                self.dictionary = u.read_file(arg)
                self.validate_dict()

            else:
                self.input = u.read_file(arg)

    # validates the limits for the dictionary
    def validate_dict(self):
        word_lengths = [len(word) for word in self.dictionary]
        unique_words = set(self.dictionary)
        min_length = min(word_lengths)
        max_length = max(word_lengths)
        # limits
        if len(unique_words) != len(self.dictionary):
            print("Dictionary off limits: Two or more words in the dictionary are the same")
            sys.exit()
        if min_length < 2 or max_length > 105:
            print("Dictionary off limits: Each word in the dictionary has to be between 2 and 105 letters long")
            sys.exit()
        if sum(word_lengths) > 105:
            print("Dictionary off limits: The sum of lengths of all words in the dictionary exceeds 105")
            sys.exit()


