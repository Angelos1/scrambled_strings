'''This class represents a dictionary word.
It breaks the dictionary word into its first
and last letters and a frequency array of the
letters in the middle
'''

import copy

class DictionaryWord:
    def __init__(self, word):
        self.word = word
        self.first_char = word[0]
        self.last_char = word[-1]
        def __freq_array(text):
            array = [0]*26
            for char in text:
                array[ord(char)-97]+=1
            return array
        self.freq_arr_middle = __freq_array(word[1:-1:])

    # def nextDictWord(self,next_letter):



    # def __freq_array(text):
    #     array =
    #     [for char in text:]

    # def play(self):
    #     return 5
    #
    # def nextDictWord(self):
# __fre
# for s in 'abcdefghijklmnopqrstuvwxyz':
#     print(ord(s)-97)