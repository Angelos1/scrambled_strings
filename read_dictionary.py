import utilities as u
import sys

class ReadDictionary:
    def __init__(self,file_path):
        self.dictionary = u.read_file(file_path)


    def validate_dict(self):
        # print(self.dictionary)
        word_lengths = [len(word) for word in self.dictionary]
        # print(word_lengths)
        unique_words = set(self.dictionary)
        min_length = min(word_lengths)
        max_length = max(word_lengths)

        # limits
        if len(unique_words) != len(self.dictionary):
            print("Dictionary off limits: Two or more words in the dictionary are the same")
            sys.exit()
        if min_length < 2 or max_length >105:
            print("Dictionary off limits: Each word in the dictionary has to be between 2 and 105 letters long")
            sys.exit()
        if sum(word_lengths) > 105:
            print("Dictionary off limits: The sum of lengths of all words in the dictionary exceeds 105")
            sys.exit()
        return self.dictionary

