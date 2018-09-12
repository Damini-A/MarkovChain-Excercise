"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    my_file = open(file_path)
    contents_of_file = my_file.read()
    
    my_file.close()


    return contents_of_file


def make_chains(text_string,number_of_grams, chains):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    words_list = text_string.split()
    
    n = number_of_grams
    for i in range(len(words_list)-1):
        
        new_ngram = words_list[i:i+n]
        

        new_ngram = tuple(new_ngram)

        if i == len(words_list) - n:
            
            if new_ngram in chains:
                chains[new_ngram] += ['']
            else:
                chains[new_ngram] = ['']
            break
        
     
        if new_ngram in chains:
            chains[new_ngram] += [words_list[i+n]]
        else:
            chains[new_ngram] = [words_list[i+n]]
   
    
    # your code goes here
    # print(chains)
    #return chains


def make_text(chains, number_of_grams):
    """Return text from chains."""

    words = []
    n = number_of_grams
    
    while True:

        first_key = choice(list(chains.keys()))
        if first_key[0][0].isupper():
            words.extend(list(first_key))
            break
        else:
            continue

    while True:
        new_key = []
        for word in words[-n:]:
            new_key.append(word)

        new_key = tuple(new_key)
        
        if new_key not in chains:
            if words[-2][-1] not in ['.', '?'] \
                or words[-2][-2] not in ['.', '?']:
                words = words[:-2]
                while True:
                    if words[-1][-1] not in ['.', '?']:
                        words = words[:-1]
                    else:
                        break  
                
            break

        new_word = choice(chains[new_key])
        words.append(new_word)

        

    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]

number_of_grams = 4

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

input_path_2 = sys.argv[2]

input_text_2 = open_and_read_file(input_path_2)

# Get a Markov chain
chains = {}
make_chains(input_text, number_of_grams, chains) 
make_chains(input_text_2, number_of_grams, chains)

#merged_chains = merge_dicts(chains_1, chains_2)

# Produce random text
random_text = make_text(chains, number_of_grams)

print(random_text)
