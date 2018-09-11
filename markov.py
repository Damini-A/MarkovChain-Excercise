"""Generate Markov text from text files."""

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


def make_chains(text_string):
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
    chains = {}

    for i in range(len(words_list)-1):
        
        new_bigram = (words_list[i], words_list[i+1])

        if i == len(words_list) - 2:
            
            if new_bigram in chains:
                chains[new_bigram] += ['']
            else:
                chains[new_bigram] = ['']
            break
        
     
        if new_bigram in chains:
            chains[new_bigram] += [words_list[i+2]]
        else:
            chains[new_bigram] = [words_list[i+2]]
   
    
    # your code goes here

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    first_key = choice(list(chains.keys()))
    words.extend(list(first_key))

    while True:

        new_key = (words[-2],words[-1])
        if new_key not in chains:
            break
        new_word = choice(chains[new_key])
        words.append(new_word)

        

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
