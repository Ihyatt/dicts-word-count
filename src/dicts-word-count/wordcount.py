# put your code here.
def count_words(path):
    path_file = open(path)
    words_dictionary = {}
   
    for line in path_file:
        for word in line.split():
            if word in words_dictionary:
                words_dictionary[word] += 1
            else: 
                words_dictionary[word] = 1

    path_file.close()

        
               
    for words, number in words_dictionary.items():
        print "%s %d" % (words,number)

count_words("test.txt")