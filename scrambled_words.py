from dictionary_word import DictionaryWord


class ScrambledWords:
    def __init__(self, dictionary, input_strings):
        self.dictionary = dictionary
        self.input_strings = input_strings

    # def curr_word_in_text(self,char_index, curr_dict_word, dict_word):
    #     curr_dict_word.first_char = self.text[char_index]
    #     curr_dict_word.last = self.text[char_index + len(dict_word) - 1]
    #     curr_dict_word.freq_arr_middle[ord(self.text[char_index])] -= 1
    #     curr_dict_word.freq_arr_middle[ord(self. text[char_index + len(dict_word) - 2])] += 1
    '''finds the next substring of the text in the input file, the one that 
    will be compared to the current dictionary_word
    '''
    def __curr_word_in_text(self, char_index, long_string, curr_dict_word, dict_word):
        # print(char_index)
        # print(char_index + len(dict_word) - 1)
        # print(ord(self.text[char_index])-97)
        # print(ord(self. text[char_index + len(dict_word) - 2])-97)
        # print(self.text[char_index])
        # print(self.text[char_index + len(dict_word) - 2])


        curr_dict_word.first_char = long_string[char_index]
        curr_dict_word.last_char = long_string[char_index + len(dict_word) - 1]
        curr_dict_word.freq_arr_middle[ord(long_string[char_index]) - 97] -= 1
        curr_dict_word.freq_arr_middle[ord(long_string[char_index + len(dict_word) - 2]) - 97] += 1

    # def algorithm(self, dictionary, input, text):
    def get_scrambled_words_occurences(self):

        line_number = 1
        for long_string in self.input_strings:
            chars_in_text = len(long_string)
            count = 0
            for dict_word in self.dictionary: # going through all the words in the dictionary
                curr_dict_word = DictionaryWord(dict_word)
                curr_word_in_text = DictionaryWord(long_string[0:len(dict_word):]) # current area of the text that we compare to the dictionary word
                for i in range(chars_in_text):
                    if (i + len(dict_word) <= chars_in_text):
                        self.__curr_word_in_text(i, long_string, curr_word_in_text, dict_word)
                        if curr_dict_word.equals(curr_word_in_text):
                            count += 1
                            break;
            print("Case #" + str(line_number) + ": " + str(count))
            line_number+=1







