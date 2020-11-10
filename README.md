# Instructions

These file contains instructions for:
* cloning the repository.
* run the program with the example files that are provided through the exercise.
* run the program with other files as inputs in order to test different scenarios.

and some extra notes on my thoughts / self-assessment.

## Clone the repository
Choose a destination folder you want to clone the repository to (e.g. *destination_folder*) and run:
```
$ cd destination_folder
$ git clone git@github.com:Angelos1/scrambled_strings.git
```

## Run the program

The program runs through a script.
It is not a running application.
Every time we call the command the application starts, prints the results and then terminates.

Run the app on your PC with the following commands:
```
$ cd scrambled_strings
$ ./scrambled-strings --dictionary Files/dictionary1 --input Files/input1
```

Inside the Files directory are all the dictionary files and input files to test the program.
**dictionary1** and **input1** are the example dictionary file and input file from the exercise respectively.

Should expect the output: **Case #1: 4**


## Run the program on the different test cases

**dictionary2** and **input2** are files I created in order to test.

**dictionary2** is as follows:
```
djhfgvjg
sdhgfjhg
jshdd
kgoi
dshbcieiufbvi
hhhhh
```
For better communication I will refer to the words of the above dictionary with their line numbers.
For example word 2 is **sdhgfjhg** and word 6 is **hhhhh**.

**input2** file is as follows:
```
lllllldjhfgvjglllllsdhgfjhglllllljshddlkgoilldshbcieiufbvillhhhhhll
lllkgoillsdhgfjhgllldjhfgvjgllllhhhhhllllllljshddllldshbcieiufbvillll
djhfgvjgllllllllllllhhhhhllldjhfgvjgllhhhhh
lljshddllllljshddlljshddlljshddlljshddllllllllllll
lllllldjghfvjglllllshhgfjdglllllljdhsdlkgoilldshbcieiufbvillhhhhhll
lllllldjghfvjglllllshhgfjdglllllljdhsdlkgoilldshbcieiufbvillhhhhhllllldjhfgvjglllsdhgfjhgllljshdd
```
In order to be able to test easier this case I followed the method below<br />
Firstly I ensured that the words in **dictionary2** do not contain the character ```l``` .<br />
Then I created **input2** file by putting the character  ```l``` wherever there is <br />
no occurrence of a word or it's scrambled version in **dictionary2**. This way I can see clearly where<br />
the words of dictionary2 appear in each line of **input2**.

For example let's take a look at the first line of **input2**: <br />
**llllll**djhfgvjg**lllll**sdhgfjhg**llllll**jshddlkgoilldshbcieiufbvi**ll**hhhhh**ll**<br />
In this line  we can see almost clearly one occurrence for each of the words of the dictionary2 file.

Analysis of the expected result if we run the program with dictionary2 and input2 files:

* *1st line of input2*: One occurrence for each of the dictionary2 words in the order that they appear in the dictionary.
   <br /> Should expect the output: **Case #1: 6**
* *2nd line of input2*: One occurrence for each of the dictionary2 words appearing in random order.
   <br /> Should expect the output: **Case #2: 6**
* *3rd line of input2*: Word 1 and word 6 of dictionary2 appearing twice each.
   <br /> Should expect the output: **Case #3: 2**
* *4th line of input2*: Word 3 of dictionary2 appearing five times.
   <br /> Should expect the output: **Case #4: 1**
* *5th line of input2*: One **scrampled** occurrence for each of the dictionary2 words.
   <br /> Should expect the output: **Case #5: 6**
* *6th line of input2*: One **scrampled** occurrence for each of the dictionary2 words and another occurrence for words 1,2 and 3.
   <br /> Should expect the output: **Case #5: 6**
   
####Run the program with dictionary2 and input2:
```
$ ./scrambled-strings --dictionary Files/dictionary2 --input Files/input2
```

Result is as described in the above analysis:
```
Case #1: 6
Case #2: 6
Case #3: 2
Case #4: 1
Case #5: 6
Case #6: 6
```

####Run the program with dictionary_sum_gt_105 :
The sum of lengths of all words in the dictionary exceeds 105 therefore it will return an error.
```
$ ./scrambled-strings --dictionary Files/dictionary_sum_gt_105 --input Files/input2
```
Returns:
```
Dictionary off limits: The sum of lengths of all words in the dictionary exceeds 105
```


####Run the program with dictionary_two_words_same :
Two words in the dictionary are the same therefore it will return an error.
```
$ ./scrambled-strings --dictionary Files/dictionary_two_words_same --input Files/input2
```
Returns:
```
Dictionary off limits: Two or more words in the dictionary are the same
```


####Run the program with dictionary_word_gt_105_chars :
A word in the dictionary is greater than 105 letters long, therefore it will return an error.
```
$ ./scrambled-strings --dictionary Files/dictionary_word_gt_105_chars --input Files/input2
```
Returns:
```
Dictionary off limits: Each word in the dictionary has to be between 2 and 105 letters long
```

####Run the program with dictionary_word_lt_2_chars :
A word in the dictionary is less than 2 letters long, therefore it will return an error.
```
$ ./scrambled-strings --dictionary Files/dictionary_word_lt_2_chars --input Files/input2
```
Returns:
```
Dictionary off limits: Each word in the dictionary has to be between 2 and 105 letters long
```

## Notes / Self assessment
I have followed the same approach described in the analysis section in Google Code Competitions (maintaining a running frequency array). 

In terms of OOP the code could have been better: More classes and methods in order to have more granular functionalities.

If I had more time I would create more classes in order to make each method do less work and unit test each one of them.
Some of these unit tests could have been for parsing a file into a list,  
finding the occurrences of a dictionary word in long_string etc.

In order to have been able to test them I would also need to make the methods return the results and not print them directly. 
That would also be a better practise for a more scalable application.