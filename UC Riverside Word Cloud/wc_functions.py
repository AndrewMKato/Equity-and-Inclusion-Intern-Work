import stylecloud as sc
from collections import Counter

def fq(txt_file_title: str, chosen_stop_words: tuple=()):
    '''Returns the frequencies of the top ten most common non-stop-words in a given text file.'''
    with open(txt_file_title, 'r') as f:
        file: list = f.readlines()

    words = []

    # Flattening file lines into the words list.
    for i in file:
        if i == '\n':
            file.remove(i)
        else:
            words_in_line: list = i.split(' ')

            for j in words_in_line:
                if j != '\n' and j not in chosen_stop_words and j.isalnum():
                    words.append(j.lower())

    Frequency = Counter(words)
    return(Frequency.most_common(10))

def wc(txt_file_title: str, png_output_title: str, chosen_stop_words: tuple=()):
    '''Uses the stylecloud library to create a word cloud output file for the provided input.'''

    sc.gen_stylecloud(
        file_path=txt_file_title, 
        output_name=png_output_title,
        icon_name='fas fa-square',
        custom_stopwords=chosen_stop_words,
        # size=2056
        )