from dictionary_word import DictionaryWord


class ScrambledWords:
    def __init__(self, dictionary, text):
        self.dictionary = dictionary
        self.text = text



    def algorithm(dictionary, text):
        chars_in_text = len(text)
        for dict_word in dictionary: # going through all the word in the dictionary
            curr_dict_word = DictionaryWord(text[0:len(dict_word):]) # current area of the text that we compare to the dictionary word
            for i in range(chars_in_text):
                if (i + len(dict_word) <= chars_in_text):
                    curr_dict_word.first_char = text[i]
                    curr_dict_word.last = text[i+len(dict_word)-1]
                    curr_dict_word.freq_arr_middle[ord(text[i])]-=1
                    curr_dict_word.freq_arr_middle[ord(text[i+len(dict_word)-2])]+=1

                len_str = len(str)



