'''This class represents a dictionary word.
It breaks the dictionary word into its first
and last letters and a frequency array of the
letters in the middle
'''


class DictionaryWord:
    def __init__(self, word):
        self.word = word
        self.first_char = word[0]
        self.last_char = word[-1]
        # def __freq_array(text):
        #     array = [0]*26
        #     for char in text:
        #         array[ord(char)-97]+=1
        #     return array
        self.freq_arr_middle = self.freq_array(word[1:-1:])

    def freq_array(self,text):
        array = [0] * 26
        for char in text:
            array[ord(char) - 97] += 1
        return array

    def equals(self, dictionary_word):
            if self.first_char == dictionary_word.first_char \
                and self.last_char == dictionary_word.last_char \
                and self.freq_arr_middle:
                return True
            else:
                return False
    def len(self):
        return len(self.word)


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