'''This class represents a dictionary word.
It breaks the dictionary word into its first
and last letters and a frequency array of the
letters in the middle
'''

class ScrambledDictionaryWord:
    def __init__(self, word):
        self.first_char = word[0]
        self.last_char = word[-1]
        self.freq_arr_middle = self.freq_array(word[1:-1:])

    # returns the frequency array of a word
    def freq_array(self,text):
        array = [0] * 26
        for char in text:
            array[ord(char) - 97] += 1
        return array

    # checks equality between ScrambledDictionaryWord objects
    def equals(self, dictionary_word):
            if self.first_char == dictionary_word.first_char \
                and self.last_char == dictionary_word.last_char \
                and self.freq_arr_middle:
                return True
            else:
                return False

