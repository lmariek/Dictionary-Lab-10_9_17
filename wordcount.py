#def function
#with open (file) as "short test"
#word_list = #for lin in file:

def get_word_counts(my_file):
    """ Counts the number of times a specific word occurs in a text file. """

    with open(my_file) as short_test:
        word_counts = {}
        # for line in short_test:
        #     line = line.rstrip()
        #     phrase = line.split()
    
        #     for word in phrase:
        #         word_counts[word] = word_counts.get(word, 0) + 1
        text = short_test.read()
        phrase = text.split()
        for word in phrase:
            word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

def print_word_counts(dictionary):
    """ Prints results from the count function. """

    for word, count in dictionary.items():
        print "{} {}".format(word, count)

# def print_word_counts(dictionary):
#     for word, count in dictionary.iteritems():
#       print "{} {}".format(word, count)

test_dict = get_word_counts("test.txt")
print_word_counts(test_dict)
